from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from accounts.forms import UserForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView,PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView,PasswordResetCompleteView
from django.contrib import messages


# Create your views here.   

def SignupPage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            print("here!!!!!!")
            forms = UserForm(request.POST)
            if forms.is_valid():
                print("2nda herwe!!!!!!!!!!!!!!!")
                forms.save()
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

class Login(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user=True


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

