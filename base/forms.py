# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Details
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1', 'password2']

class DetailsForm(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'




# class UserProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['user'] 
