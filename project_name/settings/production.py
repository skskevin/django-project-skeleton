#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*", ]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': '127.0.0.1',
#         'NAME': 'DATABASENAME',
#         'USER': 'USER',
#         'PASSWORD': 'PASSWORD',
#     }
# }

# CACHE CONFIG
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
