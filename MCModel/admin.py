from ast import Mod
from django.contrib import admin
from .models import Car, Model, Order
# Register your models here.
admin.site.register((Car, Model, Order))
