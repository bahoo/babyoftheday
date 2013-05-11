from django.contrib.syndication.views import Feed
from photos.models import Photo
from django.utils.safestring import mark_safe
from django.conf import settings


class LatestPhotos(Feed):
    title = "%s of the Day Photos" % settings.CHILD_NAME
    link = "/"
    description = "Daily photos."

    def items(self):
        return Photo.objects.order_by('-date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return mark_safe("<img src=\"%s\" /><br />%s" % (item.photo.url_125x125, item.caption))

    def __name__(self):
        return "%s of the Day" % settings.CHILD_NAME
