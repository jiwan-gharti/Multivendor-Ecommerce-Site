
from mainapp.models import Product,ProductCategory,ProductInventory,Discount,SuperProductCategory,SecondLevelCategory
from django import forms


class ProductForm(forms.ModelForm):

    
    # def add_prefix(self, field_name):
    #     # look up field name; return original if not found
    #     name = FIELD_NAME_MAPPING.get(field_name, field_name)
    #     return super(ProductForm, self).add_prefix(field_name)
    class Meta:
        model = Product
        exclude=("inventory",'discount','slug')
        # labels = {
        #     'name': 'product_name',
        # }
        # widgets = {
        #     'name': forms.TextInput()
        # }

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        exclude=("description",'slug','brand_name')

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
        fields = ("first_level_category",)
    
