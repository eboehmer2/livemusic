from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'livemusic.shows.views.homepage'),
    (r'^homepage', 'livemusic.shows.views.homepage'),
    (r'^events', 'livemusic.shows.views.events'),
    (r'^bands', 'livemusic.shows.views.bands'),
    (r'^venues', 'livemusic.shows.views.venues'),
    (r'^admin/', include(admin.site.urls)),
)


    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),


