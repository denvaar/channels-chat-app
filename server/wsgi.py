import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get("CHAT_APP_ENV", None)
if env:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.%s" % os.environ["CHAT_APP_ENV"])
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")

application = get_wsgi_application()

