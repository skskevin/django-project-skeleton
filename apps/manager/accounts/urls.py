#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^user_login/', user_login, name="user_login"),
    url(r'^login_save/', login_save, name="login_save"),
    url(r'^user_logout/', user_logout, name="user_logout"),
]
