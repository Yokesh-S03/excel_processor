"""
WSGI config for excel_processor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from apps.processor.apps import apps


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excel_processor.settings')

application = get_wsgi_application()
if __name__ == "__main__":
    apps.run()