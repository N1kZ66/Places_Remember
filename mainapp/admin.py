from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import *


@admin.register(Memories)
class ShopAdmin(OSMGeoAdmin):
    default_zoom = 5
    point_zoom = 5
    list_display = ('author', 'title', 'comment', 'location')
