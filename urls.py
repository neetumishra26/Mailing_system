from django.conf.urls.defaults import patterns, include, url
from mainapp.views import main_page

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^login/$', django.contrib.auth.views.login ),
    # Examples:
    # url(r'^$', 'mailing_system.views.home', name='home'),
    # url(r'^mailing_system/', include('mailing_system.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
