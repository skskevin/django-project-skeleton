#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import *

DEBUG = True

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'HOST': '127.0.0.1',
    #     'NAME': 'DATABASENAME',
    #     'USER': 'USER',
    #     'PASSWORD': 'PASSWORD',
    # }
}

# CACHE CONFIG
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# DJANGO DEBUG TOOLBAR
# MIDDLEWARE_CLASSES += (
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

# INSTALLED_APPS += (
#    'debug_toolbar',
# )

# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
