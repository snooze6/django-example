"""Flickr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import photos.views
import users.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', photos.views.home, name='photos_home'),
    url(r'^photos/(?P<var>[0-9]+)$', photos.views.detail, name='photos_detail'),
    url(r'^photos/new$', photos.views.new_photo, name='photo_new'),
    url(r'^login$', users.views.login, name='users_login'),
    url(r'^logout$', users.views.logout, name='users_logout'),

]
