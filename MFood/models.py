from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{}".format(self.name)
    

class Food(models.Model):
    name = models.CharField(max_length=20, null= True)
    category = models.ForeignKey(Category, models.SET_NULL, null=True)
    price = models.PositiveIntegerField(null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}".format(self.name)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk,"slug":self.name
                                               })

class OrderFood(models.Model):
    STATUS_FOOD=(
        ('Pending','pending'),
        ('Completed','completed')
    )    
    order = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)     
    ordered_by = models.ForeignKey(User, on_delete= models.CASCADE, null = True)
    ordered_on = models.DateTimeField(auto_now_add=True)
    status =models.CharField(choices=STATUS_FOOD, max_length=15)
    
    def __str__(self):
        return "{} ordered by {}".format(self.order, self.ordered_by)    