from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profile)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =['id','user','name','address','city',
    'zipcode','state']
