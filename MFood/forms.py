
from django.forms import widgets
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    
    password1 =forms.PasswordInput(attrs={
        'class':'form-control',})
    password2 =  forms.PasswordInput(attrs={
        'class':'form-control'
    })
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class FoodForm(forms.ModelForm):
        
    class Meta:
        model = Food    
        fields = ['name', 'category', 'price', 'added_by']
        widgets = {
            'name':forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),            
            'added_by': forms.Select(attrs={
                'class': 'form-control'
            }),            
        }

        
class OrderForm(forms.ModelForm):

    class Meta:
        model = OrderFood
        fields = ['order', 'ordered_by', 'status']
        widgets = {
            'order': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ordered_by': forms.Select(attrs={
                'class': 'form-control'
            }),            
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),            
        }


