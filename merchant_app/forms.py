from django.db.models import fields
from mainapp.models import Product,ProductCategory,ProductInventory,Discount,SuperProductCategory,SecondLevelCategory
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude=("inventory",'discount','slug')

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        exclude=("description",'slug')

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



class SecondLevelCategoryForm(forms.ModelForm):
    class Meta:
        model = SecondLevelCategory
        exclude = ('product_category','slug')
    
