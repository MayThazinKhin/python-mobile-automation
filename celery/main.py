from celery_config import app

# Call the task
app.send_task('celery_task.fetch_and_store_launches')
