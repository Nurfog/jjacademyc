from django.contrib import admin
from .models import *

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    imgagen = ('img', 'posicion')
    activo = ('activo')

admin.site.register(Banner, BannerAdmin)
