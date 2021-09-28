from mainapp.models import Comment, OrderItem, ShippingAddress
from accounts.models import User
from django.http import request
from django.shortcuts import redirect, render
from .forms import AddShippingAddressForm, UserForm
from myprofile.models import MyProfile

# Create your views here.

def MyProfile1(request):
    user_profile = User.objects.get(username = request.user, is_customer = True)
    print(user_profile)
    context = {
        
        'user_profile':user_profile

    }
    return render(request, "profile/myprofile.html",context)

def UpdateCustomerProfile(request):
    forms = UserForm(instance = request.user)
    if request.method == "POST":
        print("post hereeeeeee")
        forms = UserForm(request.POST, instance=request.user)
        if forms.is_valid():
            print("valid here")
            forms.save()
            return redirect("/myprofile/")
    context = {
        'forms':forms,
    }
    return render(request, "profile/update_profile.html", context)

def ShippingAddress1(request):
    context = {

    }
    return render(request, "profile/shippingaddress.html",context)

def AddShippingAddress(request):


    context = {
        # 'addsShippingForm': addsShippingForm

    }
    return render(request, "profile/AddNewShippingAddress.html",context)




def MyOrder(request):
    user = User.objects.get(id = request.user.pk, is_customer = True)
    my_order = OrderItem.object.filter(user = user, ordered = True)
    context = {
        'my_order':my_order
    }
    return render(request, "profile/my_orders.html",context)

    

def MyReview(request):
    my_reviews = Comment.objects.filter(pk = request.user.pk, user__is_customer = True)

    context = {
        'my_reviews':my_reviews
    }
    return render(request, "profile/my_review.html",context)