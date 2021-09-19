from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('register/', view=views.SignupPage, name='register'),

    path('login/', view=views.Login.as_view(), name='login'),
    path('logout/', view=LogoutView.as_view(), name='logout'),

    path('password_reset/', view = views.PasswordResetView.as_view(), name = "password_reset"),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', view = views.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
    
]