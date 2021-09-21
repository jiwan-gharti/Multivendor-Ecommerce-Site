
from django.urls import path
from . import views

app_name = "merchant_app"

urlpatterns = [
    path('',views.MerchantDashbord, name="merchant_dashboard"),
    path('api_data/',views.API_data, name="api_data")
    
]