from django.contrib.auth import authenticate, login
from django.urls.base import reverse_lazy
from accounts.forms import UserForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView,PasswordResetCompleteView
from django.contrib import messages
from .forms import LoginForm, MerchantUserForm
from .models import User
from django.contrib.auth.hashers import make_password
# from .forms import LoginForm


# Create your views here.   

def SignupPage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            print("here!!!!!!")
            forms = UserForm(request.POST)
            if forms.is_valid():
                print("2nda herwe!!!!!!!!!!!!!!!")
                forms.save(commit=False)

                username = forms.cleaned_data.get("username")
                print(username)
                first_name = forms.cleaned_data.get("first_name")
                last_name = forms.cleaned_data.get("last_name")
                email = forms.cleaned_data.get("email")
                phone_number = forms.cleaned_data.get("phone_number")
                address = forms.cleaned_data.get("address")
                gender = forms.cleaned_data.get("gender")
                password1 = forms.cleaned_data.get("password1")
                print(password1)
                password2 = forms.cleaned_data.get("password2")
                print(password2)

                user_obj = User(username = username,
                                first_name=first_name, 
                                last_name = last_name,
                                email = email,
                                phone_number = phone_number,
                                address = address,
                                gender = gender,
                                password = make_password(password1),
                                is_customer = True            

                )
                user_obj.save()


                messages.success(request, "Successfully registered your account !!!")
                return redirect(reverse("accounts:login"))
        else:
            forms = UserForm()

        
        context = {
            'forms':forms
        }
        return render(request, 'accounts/register.html', context)
    else:
        return redirect('/')

def Login(request):
    if  not request.user.is_authenticated:
    
        forms = LoginForm()

        if request.method == "POST":
            print("post request")
            forms = LoginForm(request.POST or None)
            if forms.is_valid():
                print("valid")
                username = forms.cleaned_data.get('username')
                print(username)
                password = forms.cleaned_data.get("password")
                print(password)

                user = authenticate(username = username, password = password)
                print(user)
                if user is not None:
                    print("not none")
                    login(request,user)
                    if request.user.is_authenticated and request.user.is_customer:
                        return redirect("/")
                    elif request.user.is_authenticated and  request.user.is_merchant:
                        print("merchant")
                        return redirect("/merchant/")

        context = {
            'form':forms
        }
        return render(request, 'accounts/login.html', context)
    else:
        if request.user.is_customer:
            return redirect('/')
        else:
            return redirect("/merchant/")
    



def MerchantCustomer(request):
    if not request.user.is_authenticated:
        forms = MerchantUserForm()
        if request.method == "POST":
            print("here!!!!!!")
            forms = MerchantUserForm(request.POST, request.FILES)
            if forms.is_valid():
                print("2nda herwe!!!!!!!!!!!!!!!")
                forms.save(commit=False)

                username = forms.cleaned_data.get("username")
                print(username)
                first_name = forms.cleaned_data.get("first_name")
                last_name = forms.cleaned_data.get("last_name")
                email = forms.cleaned_data.get("email")
                phone_number = forms.cleaned_data.get("phone_number")
                address = forms.cleaned_data.get("address")
                print(address)
                gender = forms.cleaned_data.get("gender")
                password1 = forms.cleaned_data.get("password1")
                print(password1)
                password2 = forms.cleaned_data.get("password2")
                print(password2)
                address = forms.cleaned_data.get("addresss")
                print(address)
                pan_no = forms.cleaned_data.get("pan_no")
                print(password2)
                document = forms.cleaned_data.get("document")
                print(document)

                user_obj = User(username = username,
                                first_name=first_name, 
                                last_name = last_name,
                                email = email,
                                phone_number = phone_number,
                                address = address,
                                gender = gender,
                                password = make_password(password1),
                                is_merchant = True,
                                pan_no =pan_no,
                                document=document


                )
                user_obj.save()
                print("merchant data saved!!!!!!")
                messages.success(request, "Successfully registered your Merchant Account !!!")
                return redirect("/accounts/login/")
        
        context = {
            'form':forms
        }
        return render(request, 'accounts/merchant_signup.html', context)
    else:
        if request.user.is_customer:
            return redirect('/')
        else:
            return redirect("/merchant/")

  




    




class PasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    # success_url = reverse_lazy('password_reset_done')

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

