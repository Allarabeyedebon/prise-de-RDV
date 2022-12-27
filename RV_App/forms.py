from tkinter import Widget
from MySQLdb import ROWID
from django import forms
from .models import *
from django.utils.safestring import mark_safe

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from allauth.account.forms import SignupForm
User = get_user_model()






# class CustomSignupForm(UserCreationForm):
#     username  = forms.CharField(max_length=50, label='Organization Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email     = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.CharField(label='Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']







# class ClientForm(forms.ModelForm):
#     class Meta:
#         model= Contact
#         fields= [
#             'name',
#             'email',
#             'sujet',
#             'message',
#             'phone'
#         ]
        
#         Widgets= {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'sujet': forms.TextInput(attrs={'class': 'form-control'}),
#             'message': forms.TextInput(attrs={'class': 'form-control', 'row':1, 'cols':30}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#         }





class ClientForm(forms.ModelForm):
    class Meta:
        model= Client
        fields= [
            'name',
            'email',
            'sujet',
            'message',
            'phone'
        ]
        
        Widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'row':1, 'cols':30}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
        






class RDVForm(forms.ModelForm):
    class Meta:
        model= RDV
        fields= [
            'client',
            'jours',
            'heure',
           
        ]
        
        Widgets= {
            'client': forms.TextInput(attrs={'class': 'form-control'}),
            'jours': forms.TextInput(attrs={'class': 'form-control'}),
            'heure':forms.NumberInput(attrs={'class':'form-control'}),
            
        }

        
        

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields= [
            'is_active',
        ]