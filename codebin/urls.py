"""codebin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from authors.views import author_login, author_logout
from django.conf import settings
from gists.views import home

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name="index"),
    url(r'^author/', include('authors.urls')),
    url(r'^login/', author_login, name="login"),
    url(r'^logout/', author_logout, name="logout"),
    url(r'^gist/', include('gists.urls')),

]


urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                    'document_root': settings.MEDIA_ROOT}))