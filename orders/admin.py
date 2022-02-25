from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

@admin.register(OrderItem)
class orderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity' ]
