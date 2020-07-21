from __future__ import absolute_import, unicode_literals

import os
import django
from . import settings
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'op_data.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
# django.setup()


app = Celery('exetask')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

