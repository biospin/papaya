"""
WSGI config for puredj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "puredj.settings")

from django.core.wsgi import get_wsgi_application
from djangae.wsgi import DjangaeApplication
application = DjangaeApplication(get_wsgi_application())
