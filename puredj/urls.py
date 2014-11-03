from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = patterns('',
    url(r'^$', lambda _ : HttpResponse('hi django')),
    # Examples:
    # url(r'^$', 'puredj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^greetings/', include('greetings.urls')),
)
