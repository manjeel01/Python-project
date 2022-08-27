from django.contrib import admin
from .models import Products, Order
from .models import Profile
from django.contrib.auth.models import Group
admin.site.site_header = 'Alpine Bio Sales and Inventory'
class productAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity')

# Register your models here.
admin.site.register(Products, productAdmin)
admin.site.register(Order)
admin.site.register(Profile)


