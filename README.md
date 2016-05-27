# django-project-skeleton
============================
## 项目简介
django-project-skeleton是用来创建django项目的模板。该模板主要包括：目录规范、后台登录APP、后台项目模板等。  

## 使用步骤

### 新建项目
```
 django-admin startproject --template=https://github.com/tudouya/django-project-skeleton/archive/master.zip [projectname]
```
或者在新建项目的同时生成Webserver配置文件: 

```
django-admin startproject --template=https://github.com/tudouya/django-project-skeleton/archive/master.zip --name apache2_vhost.sample [projectname]
```

### 配置数据库
同时配置生产和开发环境中的数据库

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'DATABASENAME',
        'USER': 'USER',
        'PASSWORD': 'PASSWORD',
    }
}

```

### 开发项目
项目开发过程。。。。。。


### 部署项目
1. 修改`manage.py`，将项目配置文件修改为`production`
2. 执行`python manage.py collectstatic`将对应静态文件搜集到`STATIC_ROOT`目录下
3. 如果在生产模式下依然使用django自带的server，需修改以`project_name/settings/urls.py`文件，将下列代码的注释去掉:  

```
# 关闭调试模式，如果未部署Nginx,则添加此URL，让Django提供静态文件
# if settings.DEBUG is False:
#     urlpatterns += [
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#     ]
```
4.修改后台登录后默认跳转的app,在`accounts`app中
