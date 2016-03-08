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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

import photos.views
import users.views
import users.api
import photos.api

# APIRouter
router = DefaultRouter()
router.register(r'api/1.0/photos', photos.api.PhotoViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', photos.views.HomeView.as_view(), name='photos_home'),
    url(r'^my_photos/$', login_required(photos.views.UserPhotosView.as_view()), name='user_photos'),
    url(r'^photos/(?P<var>[0-9]+)$', photos.views.DetailView.as_view(), name='photos_detail'),
    url(r'^photos/$', photos.views.PhotosListView.as_view(), name='photos_list'),
    url(r'^photos/new$', photos.views.CreateView.as_view(), name='photo_new'),

    url(r'', include(router.urls)),

    url(r'^login$', users.views.LoginView.as_view(), name='users_login'),
    url(r'^logout$', users.views.LogoutView.as_view(), name='users_logout'),

    url(r'^api/1.0/users/$', users.api.UserListAPI.as_view(), name='user_list_api'),
    url(r'^api/1.0/users/(?P<var>[0-9]+)$', users.api.UserDetailAPI.as_view(), name='user_details_api')
]
