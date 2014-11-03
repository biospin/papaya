# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.http import HttpResponse
import views


urlpatterns = patterns('',
                       url(r'^$', views.all_greetings),
                       url(r'^new/', views.new_greeting),
)
