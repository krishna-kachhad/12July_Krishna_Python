from django.contrib import admin
from .models import *

# Register your models here.
class studData(admin.ModelAdmin):
    list_display=['name','email','city']

admin.site.register(studinfo,studData)
