from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('tasks',
             broker='redis://127.0.0.1:6379/7',
             backend='redis://127.0.0.1:6379/9',
             include=['work.task']
             )

app.conf.update(
    result_expires=3600,
)
if __name__ == '__main__':
    app.start()
