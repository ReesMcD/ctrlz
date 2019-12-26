release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py update_index
web: gunicorn ctrlz.wsgi --log-file -
