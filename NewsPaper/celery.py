import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-weekly-news-mon-8am': {
        'task': 'news.tasks.send_weekly_news_updates',
        'schedule': crontab(hour=13, minute=54, day_of_week='wednesday'),
    },
}

app.conf.timezone = 'UTC'
