
from django import forms
# from .models import CustomerUser
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2', 'phone_number', 'gender','address']
        