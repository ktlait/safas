web: gunicorn saffap.wsgi --log-file -
worker: python manage.py rqworker high default low
