sourmash-queue
===

A queue using [celery](https://docs.celeryproject.org/) to run [https://sourmash.readthedocs.io/](sourmash) commands. 

Initially only gather supported.

It **requires** python 3.6+

Setup
---

1. Once you have cloned this repo, create a virtual environment for it
    ```shell
    python -m venv virtualenv
    source virtualenv/bin/activate
    ```
2. Install the dependencies:
    ```shell
    pip install -r requirements.txt
    ```
3. _[Optional]_ Install redis. For example:
    ```shell
    wget https://download.redis.io/releases/redis-6.2.4.tar.gz
    tar xvfs redis-6.2.4.tar.gz
    ```
   Edit its config to make it available from a different VM and disable protected-mode.

   And run the service:
    ```shell
    ./redis-6.2.4/src/redis-server redis-6.2.4/redis.conf
    ```
   
4. Edit the settings.py file to point to the right paths.
5. Start the celery worker
    ```shell
   nohup celery -A tasks worker --loglevel=INFO > celery.log &
    ```
   **⚠️TODO**: Setup this as a [systemd](https://docs.celeryproject.org/en/latest/userguide/daemonizing.html?highlight=celerybeat#usage-systemd) or something more reliable
