from django.contrib import admin
from models import Photo


class PhotoAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    pass

admin.site.register(Photo, PhotoAdmin)
