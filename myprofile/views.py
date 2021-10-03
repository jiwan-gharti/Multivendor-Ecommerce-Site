from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mainapp.models import Comment, OrderItem
from accounts.models import User
from django.shortcuts import redirect, render
from .forms import UserForm
from myprofile.models import MerchantReview

# Create your views here.
@login_required
def MyProfile1(request):
    if request.user.is_customer:
        user_profile = User.objects.get(username = request.user, is_customer = True)
        print(user_profile)
        context = {
            
            'user_profile':user_profile

        }
        return render(request, "profile/myprofile.html",context)
    else:
        messages.info(request, "Access Denied! please Login as Customer.")
        return redirect("/")

@login_required
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
    if request.user.is_customer:
        return render(request, "profile/update_profile.html", context)
    else:
        messages.info(request, "Access Denied! please Login as Customer.")
        return redirect("/")

@login_required
def ShippingAddress1(request):
    context = {

    }
    if request.user.is_customer:
        return render(request, "profile/shippingaddress.html",context)
    else:
        messages.info(request, "Access Denied! please Login as Customer.")
        return redirect("/")

login_required
def AddShippingAddress(request):


    context = {
        # 'addsShippingForm': addsShippingForm

    }
    if request.user.is_customer:
        return render(request, "profile/AddNewShippingAddress.html",context)
    else:
        messages.info(request, "Access Denied! please Login as Customer.")
        return redirect("/")



@login_required
def MyOrder(request):
    if request.user.is_customer:
        user = User.objects.get(id = request.user.pk, is_customer = True)
        my_order = OrderItem.object.filter(user = user, ordered = True)
        context = {
            'my_order':my_order
        }
    
        return render(request, "profile/my_orders.html",context)
    else:
        messages.info(request, "Access Denied! please Login as Customer.")
        return redirect("/")

    

@login_required
def MyReview(request):
    my_reviews = Comment.objects.filter(pk = request.user.pk, user__is_customer = True)

    context = {
        'my_reviews':my_reviews
    }
    if request.user.is_customer:
        return render(request, "profile/my_review.html",context)
    else:
        messages.info(request, "Access Denied! please Login as Customer.")
        return redirect("/")

def ReviewSeller(request):

    ordered_items = OrderItem.objects.filter(user= request.user, received = True)
    print(ordered_items)
    ordered_items = ordered_items.exclude(merchantreview__is_rated = True)
    print(ordered_items)
    # print(ordered_items)
    # for order in ordered_items:
    #     print(order.merchantreview_set)

    context = {
        'ordered_items':ordered_items

    }
    return render(request,'profile/review_merchant.html', context)
    


def ReviewSeller1(request,pk):
    if request.method == 'POST':
        rate = request.POST.get('rate')

        product = OrderItem.objects.get(pk = pk)

        merchant_rate_obj = MerchantReview.objects.create(
                                                        user = product.item.user,
                                                        product = product,
                                                        rate = rate,
                                                        is_rated = True
                                                        )
        merchant_rate_obj.save()
        
        return redirect("/myprofile/review_seller/")
