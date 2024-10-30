from celery import Celery

app = Celery('tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    result_expires=3600,
    task_acks_on_failure_or_timeout=True,
    task_reject_on_worker_lost=True,
    task_track_started=True,
    worker_prefetch_multiplier=1,
    task_annotations={'*': {'rate_limit': '10/s'}}
)
