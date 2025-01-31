import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reefs_news.settings")
django.setup()

from django.core.management import call_command

call_command('flush', interactive=False)
