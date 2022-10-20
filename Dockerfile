FROM python:3.8-bullseye

COPY requirements.txt /opt/app/

RUN pip3 install -r /opt/app/requirements.txt

RUN mkdir -p /opt/sourmash/queries
RUN mkdir -p /opt/sourmash/signatures/human-gut-v2-0
RUN mkdir -p /opt/sourmash/results

WORKDIR /opt/app
CMD celery -A tasks worker --loglevel=INFO
