import os
from thumbs import ImageWithThumbsField
from datetime import datetime
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify


def image_filename(instance, filename):
    base_dir = 'images/'
    base_name, extension = os.path.splitext(filename)
    title = instance.date.strftime('%Y%m%d') + '-' + slugify(instance.title)
    return "%s%s%s" % (base_dir, title, extension)

class Photo(models.Model):
    photo = ImageWithThumbsField(upload_to=image_filename, sizes=((125, 125), (600, 450),))
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=140, blank=True)

    def save(self, **kwargs):
        if not self.id:
            self.date = datetime.now()
        super(Photo, self).save()

    class Meta:
        get_latest_by = "date"
        ordering = ['-date']

    def get_absolute_url(self):
        return ('photo_detail', None, {
                'year': self.date.strftime('%Y'),
                'month': self.date.strftime('%b').lower(),
                'day': self.date.strftime('%d'),
                'pk': self.id})
    get_absolute_url = permalink(get_absolute_url)

    def get_full_url(self):
        current_domain = Site.objects.get_current().domain
        return 'http://%s%s' % (current_domain, self.get_absolute_url())

    def __unicode__(self):
        return "%s | %s - %s" % (self.date.strftime('%Y-%m-%d'), self.title, self.caption)
