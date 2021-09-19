from django.http import request
from django.shortcuts import render

# Create your views here.

def MyProfile(request):
    context = {

    }
    return render(request, "profile/myprofile.html",context)


def ShippingAddress(request):

    context = {

    }
    return render(request, "profile/shippingaddress.html",context)

def AddShippingAddress(request):
    context = {

    }
    return render(request, "profile/AddNewShippingAddress.html",context)



