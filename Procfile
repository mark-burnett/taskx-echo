web: gunicorn echo.wsgi --log-file -
worker: celery worker --app=echo.celery.app
