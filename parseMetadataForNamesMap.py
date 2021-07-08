import csv
import json

metadata_path="genomes-all_metadata.tsv"

metadata_output_path="genomes-gut_metadata.json"

names_map = {}
with open(metadata_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        names_map[row['Genome']] = row['MGnify_accession']

# print(names_map)
with open(metadata_output_path, 'w') as jsonfile:
    json.dump(names_map,jsonfile)
