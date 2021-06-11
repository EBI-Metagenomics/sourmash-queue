# Replace this for the full path of where the folders with the data for sourmash is going to be stored
BASE_PATH = "./"

# Folder where the signatures to use as query are going to be
QUERIES_PATH = f"{BASE_PATH}/queries/"

# The index file that hold the inormations of the signatures to search against
SIGNATURES_PATH = f"{BASE_PATH}/signatures/genomes_index.sbt.json"
# Folder where the results of sourmash are going to be stored
RESULTS_PATH = f"{BASE_PATH}/results/"

# Path to the broker URL to run celery. Defaults to use redix in localhost
CELERY_BROKER_PATH = "redis://localhost:6379/0"
# Path to the backend URL to run celery. Defaults to use redix in localhost
CELERY_BACKEND_PATH = "redis://localhost:6379/1"
