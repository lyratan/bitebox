from django.contrib import admin
from . models import Customer, Food, Order

# Register your models here.
admin.site.register([Customer, Food, Order])