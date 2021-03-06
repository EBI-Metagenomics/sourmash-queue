# Replace this for the full path of where the folders with the data for sourmash is going to be stored
BASE_PATH = "./"

# Folder where the signatures to use as query are going to be
QUERIES_PATH = f"{BASE_PATH}/queries/"

# The The folder wher the signatures of all the catalog are stored
SIGNATURES_PATH = f"{BASE_PATH}/signatures/"

# Folder where the results of sourmash are going to be stored
RESULTS_PATH = f"{BASE_PATH}/results/"

# The currently supported catalogs
MAG_CATALOGS = {
    "human-gut-v1-0": f"{SIGNATURES_PATH}HGUT/genomes_index.sbt.json"
}

# Path to the broker URL to run celery. Defaults to use redix in localhost
CELERY_BROKER_PATH = "redis://localhost:6379/0"
# Path to the backend URL to run celery. Defaults to use redix in localhost
CELERY_BACKEND_PATH = "redis://localhost:6379/1"

# The names of the sourmash files are GUT_GENOME* but the MGnify ID is MGYG-HGUT-* This file is a mapping between this 2 accessions
MAP_NAMES_PATH = f"{BASE_PATH}/genomes-gut_metadata.json"

# Saved results in redis will expire on
RESULTS_EXPIRE = 60 * 60 * 24 * 30  # 30 days
