from django.contrib import admin
from .models import *

# Register your models here.
class commentData(admin.ModelAdmin):
    list_display=['title','content','created_at','updates_at']

admin.site.register(comment,commentData)
