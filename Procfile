release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn ctrlz.wsgi --log-file -
