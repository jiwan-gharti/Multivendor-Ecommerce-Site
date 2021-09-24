from mainapp.models import Comment
from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from phonenumber_field.formfields import PhoneNumberField


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

DISTRICT_CHOICES = [
    ('kathmandu', 'kathmandu'),
    ('Pokhara','Pokhara'),
    ('Dhangadi','Dhangadi'),
    ('Butwal','Butwal'),
    ('Aacham','Aacham'),
    ('Jhapa','Jhapa'),
    ('Gulmi', "Gulmi")
]

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    email     =  forms.EmailField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number  = PhoneNumberField(help_text ="Required: Country Code(+977)", required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_district = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class':'form-control'}), choices=DISTRICT_CHOICES)
    shipping_address2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}) )
    shipping_zip = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    # same_billing_address = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-control'}))

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("subject", "comment","rate")
    
