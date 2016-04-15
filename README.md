django-project-skeleton
=======================
Usage
-----

To use this repository just use the ``template`` option of `django-admin
<https://docs.djangoproject.com/en/1.8/ref/django-admin/#startproject-projectname-destination>`_::

    $ django-admin startproject --template=https://github.com/tudouya/django-project-skeleton/archive/master.zip [projectname]

If you wish to automagically fill the ``apache2_vhost.sample`` the command is::

    $ django-admin startproject --template=https://github.com/tudouya/django-project-skeleton/archive/master.zip --name apache2_vhost.sample [projectname]
