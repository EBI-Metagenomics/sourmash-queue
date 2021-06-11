from celery import Celery
from sourmash.commands import gather
from settings import *

app = Celery('tasks', broker=CELERY_BROKER_PATH, backend=CELERY_BACKEND_PATH)


@app.task(bind=True)
def run_gather(self, query_filename):
    args = type('', (), {})()
    args.query = f"{QUERIES_PATH}{query_filename}"
    args.databases = [SIGNATURES_PATH]
    args.output = f"{RESULTS_PATH}{self.request.id}.csv"
    args.ksize = 31
    args.dna = True
    args.dayhoff = False
    args.hp = False
    args.protein = False
    args.prefetch = True
    args.quiet = True
    args.debug = False
    args.threshold_bp = 5e4
    args.num_results = None
    args.md5 = None
    args.scaled = 0
    args.cache_size = 0
    args.linear = False
    args.save_prefetch = None
    args.ignore_abundance = False
    args.save_matches = False
    args.output_unassigned = False

    gather(args)
