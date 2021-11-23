web: gunicorn socialMedia.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1
python manage.py collectstatic --noinput
manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT project_name:socialMedia