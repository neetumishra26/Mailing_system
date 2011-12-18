from django.conf.urls.defaults import patterns, include, url
from mainapp.views import main_page, logout_page

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^login/$', 'django.contrib.auth.views.login' ),
    (r'^logout/$', logout_page ),
)
