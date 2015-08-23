__author__ = 'oguzhansagoglu'
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create$', views.register, name='register_author'),
]
