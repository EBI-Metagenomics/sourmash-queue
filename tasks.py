from celery import Celery
import csv
from sourmash.sourmash_args import load_query_signature, load_dbs_and_sigs, FileOutputCSV, \
    get_moltype
from sourmash.search import format_bp, gather_databases
from sourmash.commands import SaveSignaturesToLocation
from settings import *

DEBUG = True


def notify(text):
    if DEBUG:
        print(text)


app = Celery('tasks', broker=CELERY_BROKER_PATH, backend=CELERY_BACKEND_PATH)

fieldnames = ['intersect_bp', 'f_orig_query', 'f_match',
              'f_unique_to_query', 'f_unique_weighted',
              'average_abund', 'median_abund', 'std_abund', 'name',
              'filename', 'md5', 'f_match_orig', 'unique_intersect_bp',
              'gather_result_rank', 'remaining_bp',
              'query_filename', 'query_name', 'query_md5', 'query_bp']


@app.task(bind=True)
def run_gather(self, query_filename, original_filename, catalog):
    # adapting from sourmash gather command 4.1.2
    # https://github.com/sourmash-bio/sourmash/blob/01de852439153267b7956e818fd90bb26c87e0ac/src/sourmash/commands.py#L614

    if catalog not in MAG_CATALOGS:
        raise Exception(f"The request doesn't include a valid catalog. It has to be one of {MAG_CATALOGS.keys()}")

    moltype = 'DNA'
    cache_size = None
    # linear = False
    # prefetch = True
    save_prefetch = None
    threshold_bp = 5e4
    # is_abundance = False
    ignore_abundance = False

    query = load_query_signature(f"{QUERIES_PATH}{query_filename}", ksize=31, select_moltype=moltype)

    notify(f'loaded query: {str(query)[:30]}... (k={query.minhash.ksize}, {get_moltype(query)})')

    # verify signature was computed right.
    if not query.minhash.scaled:
        raise Exception("query signature needs to be created with --scaled")

    # downsample is not implemented here

    # empty?
    if not len(query.minhash):
        raise Exception('no query hashes!? exiting.')

    #
    databases = load_dbs_and_sigs([MAG_CATALOGS[catalog]], query, False,
                                  cache_size=cache_size)

    if not len(databases):
        raise Exception('Nothing found to search!')

    prefetch_query = query.copy()
    prefetch_query.minhash = prefetch_query.minhash.flatten()
    save_prefetch = SaveSignaturesToLocation(save_prefetch)
    save_prefetch.open()

    counters = []
    for db in databases:
        counter = db.counter_gather(prefetch_query, threshold_bp)
        save_prefetch.add_many(counter.siglist)
        counters.append(counter)

    notify(f"Found {len(save_prefetch)} signatures via prefetch; now doing gather.")
    save_prefetch.close()

    ## ok! now do gather -
    found = []
    # weighted_missed = 1
    # orig_query_mh = query.minhash
    # next_query = query
    first_match = None

    gather_iter = gather_databases(query, counters, threshold_bp,
                                   ignore_abundance)

    for result, weighted_missed, next_query in gather_iter:
        pct_query = '{:.1f}%'.format(result.f_unique_weighted * 100)
        pct_genome = '{:.1f}%'.format(result.f_match * 100)
        name = result.match.filename
        if not len(found):  # first result?
            first_match = {
                "overlap": format_bp(result.intersect_bp),
                "p_query": pct_query,
                "p_match": pct_genome,
                "match": name,
                "query_filename": original_filename,
                "md5_name": query_filename,
            }
            found.append(result)
        if len(found) == 0:
            return {
                "status": "NO_RESULTS",
                "query_filename": original_filename,
                "md5_name": query_filename,
            }
        else:
            with FileOutputCSV(f"{RESULTS_PATH}{self.request.id}.csv") as fp:
                w = csv.DictWriter(fp, fieldnames=fieldnames, extrasaction='ignore')
                w.writeheader()
                for result in found:
                    d = dict(result._asdict())
                    if "match" in d:
                        del d['match']  # actual signature not in CSV.
                        w.writerow(d)
        return first_match
