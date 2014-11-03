# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.http import HttpResponse


urlpatterns = patterns('',
                       url(r'^$', lambda _ : HttpResponse('welcome greetings')),
)
