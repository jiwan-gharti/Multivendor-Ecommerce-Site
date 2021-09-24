
from django.urls import path
from . import views

app_name = "merchant_app"

urlpatterns = [
    path('',views.MerchantDashbord, name="merchant_dashboard"),
    path('api_data/',views.API_data, name="api_data"),
    path("delete_product/<int:pk>/",views.DeleteProduct,name="delete_product"),
    path("update_product/<int:pk>/",views.UpdateProduct,name="update_product"),
    path("logout/",views.Logout,name="logout"),
    path("mprofile_update/", views.mProfileUpdate, name = "mProfile_upadate")


    
]