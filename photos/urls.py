from django.conf.urls import include, patterns, url
from django.shortcuts import render
from photos.views import PhotoArchiveIndexView, PhotoYearArchiveView, PhotoMonthArchiveView, PhotoDayArchiveView, PhotoDateDetailView
from photos.feeds import LatestPhotos

urlpatterns = patterns('',
                    url(r'^feed/', LatestPhotos(), {}, name='rss_feed'),
                    url(r'^archives/$', PhotoArchiveIndexView.as_view(), name='photo_archive_index'),
                    url(r'^archives/page/(?P<page>[0-9]+)/$$', PhotoArchiveIndexView.as_view(), name='photo_archive_index'),
                    url(r'^archives/(?P<year>\d{4})/$', PhotoYearArchiveView.as_view(), name='photo_year_archive'),
                    url(r'^archives/(?P<year>\d{4})/(?P<month>\w{3})/$', PhotoMonthArchiveView.as_view(), name='photo_month_archive'),
                    url(r'^archives/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d+)/$', PhotoDayArchiveView.as_view(), name='photo_day_archive'),
                    url(r'^archives/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d+)/photo-(?P<pk>\d+)/$', PhotoDateDetailView.as_view(), name="photo_detail"),
                    url(r'^pages/', include('django.contrib.flatpages.urls')),
                    url(r'^favicon\.ico$', 'django.shortcuts.redirect', {'to': '/static/img/favicon.png'}),
                    url(r'^robots\.txt$', render, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
                    url(r'^$', 'photos.views.home', name="home"),
)
