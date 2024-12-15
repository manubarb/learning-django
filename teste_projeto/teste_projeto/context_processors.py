# meuapp/context_processors.py
from django.conf import settings

def app_version(request):
    return {'version': settings.VERSION}
