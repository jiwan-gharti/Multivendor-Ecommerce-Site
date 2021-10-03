
from django.forms import widgets
from accounts.models import User
from mainapp.models import ContactUS, Product,ProductInventory,Discount
from django import forms
from django_summernote.widgets import SummernoteWidget


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude=("inventory",'discount','slug','user')
        widgets = {
            # 'short_description': SummernoteWidget(),
            'description':SummernoteWidget(),
            
        }



class ProductInventoryForm(forms.ModelForm):
    class Meta:
        model = ProductInventory
        fields = '__all__'

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        exclude = ('slug',)
        widgets = {
            'name': forms.TextInput(attrs={'name':'discount_name'}),
            'description': forms.TextInput(attrs={'name':'discount_description'}),
            
        }



class MerchantProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", 'last_name', 'email', 'phone_number','pan_no','document')


