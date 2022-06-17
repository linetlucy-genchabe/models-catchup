from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Favorite_artist)
admin.site.register(Tags)
admin.site.register(Album)
admin.site.register(Song)