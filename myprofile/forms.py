
from django import forms
from django.forms import fields
from mainapp.models import User,ShippingAddress

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'phone_number','address','gender')

class AddShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = "__all__"