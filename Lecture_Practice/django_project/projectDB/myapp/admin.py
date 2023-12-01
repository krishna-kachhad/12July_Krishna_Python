from django.contrib import admin
from .models import *

# Register your models here.
class userdata(admin.ModelAdmin):
    ordering=['firstname']
    list_display=['firstname','lastname','email','dob']


    
admin.site.register(userinfo,userdata)
admin.site.register(studentinfo)
