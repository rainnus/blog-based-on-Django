#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *


urlpatterns = patterns(('myapp.views'),
    url(r'^bloglist/$', 'blog_list', name='bloglist'),
    url(r'^blog/(?P<id>\d+)/$', 'blog_show', name='detailblog'),
    url(r'^blog/(?P<id>\d+)/commentshow/$', 'blog_show_comment', name='showcomment'),
)