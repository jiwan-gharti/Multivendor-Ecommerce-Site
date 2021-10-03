
from django import forms
# from .models import CustomerUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import User
from django.forms import ValidationError
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2', 'phone_number', 'gender','address',]
    
    

class MerchantUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2', 'shop_name','phone_number', 'gender','address','pan_no','document']

    def clean_pan_no(self):
        pan_no = self.cleaned_data['pan_no']
        print(pan_no)
        print(type(pan_no))
        if len(str(pan_no)) != 9:
            raise ValidationError("Pan number must be 9 digits!")

        return pan_no


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )        