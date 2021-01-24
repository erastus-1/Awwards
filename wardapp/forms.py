from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'image'] 

class ProjectForm(forms.ModelForm):

    class Meta:
        model= Projects
        fields= ['user', 'image', 'title', 'description', 'link','post_date', 'technologies']   