from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView
from django.shortcuts import render
from photos.models import Photo


class PhotoMixin(object):
    date_field = "date"
    model = Photo


class PhotoArchiveIndexView(PhotoMixin, ArchiveIndexView):
    date_list_period = "month"
    paginate_by = 20


class PhotoYearArchiveView(PhotoMixin, YearArchiveView):
    make_object_list = True


class PhotoMonthArchiveView(PhotoMixin, MonthArchiveView):
    pass


class PhotoDayArchiveView(PhotoMixin, DayArchiveView):
    pass


class PhotoDateDetailView(PhotoMixin, DateDetailView):
    pass


def home(request, *args, **kwargs):
    photo_list = Photo.objects.all()[0:9]
    return render(request, 'photos/home.html', {'photo_list': photo_list})
