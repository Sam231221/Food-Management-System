from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
     path('', fooddetail_view, name="foods"),
     
     path('food/create', foodcreate_view, name="foodcreate"),
     path('food/delete', fooddelete_view, name="fooddelete"),
     path('food/update', foodupdate_view, name="foodupdate"),

     path('order/create', ordercreate_view, name="ordercreate"),


]
