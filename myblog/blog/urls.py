#coding: utf-8
from django.core.urlresolvers import reverse

__author__ = 'kirill'

from django.conf.urls import patterns, url, include
from views import PostsListView, PostDetailView

urlpatterns = patterns('',

url(r'^$', PostsListView.as_view(), name='list'),
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
)
