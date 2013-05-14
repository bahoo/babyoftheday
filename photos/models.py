from django.db import models
from thumbs import ImageWithThumbsField
from django.db.models import permalink
from datetime import datetime
from django.contrib.sites.models import Site


class Photo(models.Model):
    # photo = models.ImageField(upload_to='photos')
    # web = models.ImageField(upload_to='photos')
    # thumb = models.ImageField(upload_to='photos')
    photo = ImageWithThumbsField(upload_to='images', sizes=((125, 125), (600, 450),))
    date = models.DateTimeField()
    title = models.CharField(max_length=50, default='Untitled')
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
