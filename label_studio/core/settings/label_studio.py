"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
from core.settings.base import *

DJANGO_DB = get_env('DJANGO_DB', DJANGO_DB_SQLITE)
DATABASES = {'default': DATABASES_ALL[DJANGO_DB]}

MIDDLEWARE.append('organizations.middleware.DummyGetSessionMiddleware')
MIDDLEWARE.append('core.middleware.UpdateLastActivityMiddleware')

ADD_DEFAULT_ML_BACKENDS = False

LOGGING['root']['level'] = get_env('LOG_LEVEL', 'DEBUG')

DEBUG = get_bool_env('DEBUG', False)

DEBUG_PROPAGATE_EXCEPTIONS = get_bool_env('DEBUG_PROPAGATE_EXCEPTIONS', False)

SESSION_COOKIE_SECURE = False

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

RQ_QUEUES = {}

SENTRY_DSN = get_env('SENTRY_DSN', 'https://44f7a50de5ab425ca6bc406ef69b2122@o227124.ingest.sentry.io/5820521')
SENTRY_ENVIRONMENT = get_env('SENTRY_ENVIRONMENT', 'opensource')

from label_studio import __version__
from label_studio.core.utils import sentry
sentry.init_sentry(release_name='label-studio', release_version=__version__)

# we should do it after sentry init
from label_studio.core.utils.common import collect_versions
versions = collect_versions()

# YoDa Customs
YODA_GOOGLE_OAUTH_ENABLE = get_bool_env('YODA_GOOGLE_OAUTH_ENABLE', False)
YODA_GOOGLE_CLIENT_ID = get_env('YODA_GOOGLE_CLIENT_ID')
YODA_GOOGLE_CLIENT_SECRET = get_env('YODA_GOOGLE_CLIENT_SECRET')

SITE_ID = 1
LOGIN_REDIRECT_URL = '/projects'
LOGOUT_REDIRECT_URL = '/'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': YODA_GOOGLE_CLIENT_ID,
            'secret': YODA_GOOGLE_CLIENT_SECRET,
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}