__author__ = 'alex'

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'social.apps.django_app.default',
)

PYTHONMID_APPS = (
    'pythonmid.apps.security',
    'pythonmid.apps.events',
    'pythonmid.apps.community',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PYTHONMID_APPS