web: gunicorn taskx_service.wsgi --log-file -
worker: celery worker --app=taskx_service.celery.app
