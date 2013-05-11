from django.conf.urls import include, patterns
from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView
from photos.models import Photo
from photos.views import *
from feeds import LatestPhotos

urlpatterns = patterns('',
                    (r'^feed/', LatestPhotos(), {}, 'rss_feed'),
                    (r'^archives/$', ArchiveIndexView.as_view(model=Photo, date_field='date'), dict(extra_context={'months': Photo.objects.dates('date', 'month')}), 'photo_archive_index'),
                    (r'^archives/(?P<year>\d{4})/$', YearArchiveView.as_view(), dict(photo_dict, make_object_list=True), 'photo_year_archive'),
                    (r'^archives/(?P<year>\d{4})/(?P<month>\w{3})/$', MonthArchiveView.as_view(), dict(photo_dict, allow_empty=True), 'photo_month_archive'),
                    (r'^archives/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d+)/$', DayArchiveView.as_view(), dict(photo_dict, allow_empty=True), 'photo_day_archive'),
                    (r'^archives/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d+)/photo-(?P<object_id>\d+)/$', DateDetailView.as_view(), photo_dict, 'photo_detail'),
                    (r'^pages/', include('django.contrib.flatpages.urls')),
                    (r'^favicon\.ico$', 'django.shortcuts.redirect', {'to': '/static/img/favicon.png'}),
                    (r'^robots\.txt$', render, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
                    (r'^$', home, photo_dict, 'home'),
)
