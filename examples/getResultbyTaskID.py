from celery import Celery

app = Celery('tasks', broker="redis://mgnify-sourmash:6379/0", backend="redis://mgnify-sourmash:6379/1")
r = app.AsyncResult('d091aa26-86ed-48a6-b1ab-755a73d2a313')
print(f"Task ID: {r.id}")
print(f"STATUS: {r.status}")
