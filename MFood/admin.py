from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin,ImportMixin , ImportExportModelAdmin  
from .models import Category, Food, OrderFood

#package url: https://django-import-export.readthedocs.io/en/stable/getting_started.html

#create a ModelResource class in admin.py that will describe how this resource can be imported or exported:
'''
Best Configuration for exporting data only. Note we can't import this data back to django since we 
dehydrate fields to the readable format.
class FoodResource(resources.ModelResource):
    added_by = Field()
    added_on = Field()
    category = Field()
    class Meta:
        model = Food
        fields = ('id', 'name', 'category', 'price', 'added_by',  'added_on')
        #export_order = ('id', 'price', 'category', 'name') #ordering
        
    def dehydrate_added_by(self, obj): #dehydrate_<field_name>
        return str(obj.added_by.username)    
    
    def dehydrate_added_on(self,obj):
        return obj.added_on.strftime('%d-%m-%Y')
    
    def dehydrate_category(self,obj):
        return obj.category.name
        
class FoodAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = FoodResource


'''

'''
Best Configuration for import export. Note Relationships are rendererd by id field that can be 
imported back. However You need to have those objects that are pre-existing in the database.
For example:
       If we wanna import  .csv file containing food objects, We must have category and user obj of same id
       already in the database. Otherwise, we''ll recieve Error.
       
       The solution is we need to export each and every objects that has relationship with each other. Then
       Import those ojects via .csv or .xls in a certain sequential order.
       
Also Note that importing functionality of  django-import-export package imports by id if it.    
'''


class FoodResource(resources.ModelResource):
    class Meta:
        model = Food
        fields = ('id', 'name', 'category', 'price', 'added_by',  'added_on')
        
class FoodAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FoodResource
        

    
admin.site.register(Food, FoodAdmin)    
admin.site.register((Category, OrderFood))    
  