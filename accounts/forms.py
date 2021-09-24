
from django import forms
# from .models import CustomerUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2', 'phone_number', 'gender','address',]

class MerchantUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2', 'phone_number', 'gender','address','pan_no','document']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )        