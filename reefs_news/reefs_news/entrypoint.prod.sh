python manage.py collectstatic
python manage.py migrate --noinput
python manage.py -m gunicorn --bind 0.0.0.0:8000 --workers 3 reefs_news