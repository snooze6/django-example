from django.contrib import admin
from photos.models import Photo

# Register your models here.

admin.site.register(Photo)

class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner', 'license', 'visibility')