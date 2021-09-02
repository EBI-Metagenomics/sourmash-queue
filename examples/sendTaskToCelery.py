from celery import Celery

app = Celery('tasks', broker="redis://localhost:6379/0", backend="redis://localhost:6379/1")
r = app.send_task('tasks.run_gather', ('8a2b9f64bb476965359344d1fb83a6b1.sig', 'JAFQLC01.fasta', 'human-gut-v1-0'))

print(f"Task ID: {r.id}")
print(f"STATUS: {r.status}")
