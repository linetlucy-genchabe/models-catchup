from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.




admin.site.register(Favorite_artist)
admin.site.register(Tags)
admin.site.register(Album)
admin.site.register(Song)