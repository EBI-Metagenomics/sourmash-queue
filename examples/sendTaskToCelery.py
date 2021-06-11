from celery import Celery

app = Celery('tasks', broker="redis://mgnify-sourmash:6379/0", backend="redis://mgnify-sourmash:6379/1")
r = app.send_task('tasks.run_gather', ('q1.sig',))
print(f"Task ID: {r.id}")
print(f"STATUS: {r.status}")
