from django.contrib import admin
from django.urls import path
from .views import dashboard_view, foodcreate_view,fooddelete_view, ordercreate_view, search_engine, foodupdate_view
urlpatterns = [
     path('', dashboard_view, name="dashboard"),
     
     #FOOD CRUD
     path('food/create', foodcreate_view, name="foodcreate"),
     path('food/delete', fooddelete_view, name="fooddelete"),
     path('food/update', foodupdate_view, name="foodupdate"),

     #ORDER CRUD 
     path('order/create', ordercreate_view, name="ordercreate"),
     
     path('search_results', search_engine, name="search_engine")

]
