from django.contrib import admin
from .models import Landmark, LandmarkPhoto

class LandmarkPhotoInline(admin.TabularInline):
    model = LandmarkPhoto
    extra = 1

@admin.register(Landmark)
class LandmarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    inlines = [LandmarkPhotoInline]

@admin.register(LandmarkPhoto)
class LandmarkPhotoAdmin(admin.ModelAdmin):
    list_display = ('landmark', 'caption', 'order')
    list_filter = ('landmark',)
    search_fields = ('landmark__name', 'caption')
