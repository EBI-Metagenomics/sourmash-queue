Examples to execute sourmash in the queue
===

The example scripts in this directory can be run from any machine that has access to the instance
of redis use to setup the queue.

The scripts assume the signature to query is in the QUERIES_PATH that has been set in the settings.

Remember to install the [requirements](./requirements.txt) in the environment where this scripts will be run.

`sendTaskToCelery.py`
---
This submits a task(`run_gather`) to the queue. Just make sure the broker and backend are well defined in the script.

`getResultbyTaskID.py`
---
Using a task ID, such as the one obtained with `sendTaskToCelery.py`, we can check the status of that task in the queue.

If the task is successful there should be a CSV file in the `RESULTS_PATH` which name is `{id}.csv`, where `{id}` is the id requested.