from django.urls import path
from . import views

app_name = "myprofile"

urlpatterns = [
    path("", view=views.MyProfile, name="profile"),
    path("shippingaddress/", view=views.ShippingAddress, name="shippingaddress"),
    path("addshippingaddress/", view=views.AddShippingAddress, name="add-shipping-address")
]
