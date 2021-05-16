from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def homepage(request):
    return render (request, 'mainapp/homepage.html')

def details(request):
    return render (request, 'mainapp/details.html')

class CartTemplate(TemplateView):
    template_name = 'mainapp/cart.html'

class ContactUs(TemplateView):
    template_name = 'mainapp/contactus.html'

class AboutUs(TemplateView):
    template_name = 'mainapp/aboutus.html'

class ShoppingPage(TemplateView):
    template_name = 'mainapp/shopping_page.html'
  
class CheckoutPage(TemplateView):
    template_name = 'mainapp/checkoutpage.html'