#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def user_login(request):
    # 如果已登录，直接进入后台首页
    if request.user.is_authenticated():
        return HttpResponseRedirect('/example/index')

    return render(request, 'manager/accounts/user_login.html')


def login_save(request):
    if 'POST' == request.method:
        username = request.POST['username']
        password = request.POST['password']
        print request.POST['password']
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)

            return HttpResponseRedirect('/example/index')
        else:
            return HttpResponseRedirect('/accounts/user_login')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/user_login')
