from django.forms  import ModelForm, fields
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']