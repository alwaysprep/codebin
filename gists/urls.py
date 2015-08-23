from .views import create

__author__ = 'oguzhansagoglu'
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<gi>[\w-]+)/$', create, name='create_gist'),
    url(r'^(?P<gi>[\w-]+)/(?P<snip>[\w-]+)/$', create, name='create_gist'),
    url(r'^$', create, name='create_gist'),

]

