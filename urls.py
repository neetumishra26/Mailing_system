from django.conf.urls.defaults import patterns, include, url
from mainapp.views import main_page, logout_page, compose_mail

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^login/$', 'django.contrib.auth.views.login' ),
    (r'^logout/$', logout_page ),
    (r'^compose/$', compose_mail ),
)
