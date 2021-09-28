from django.urls import path
from . import views

app_name = "myprofile"

urlpatterns = [
    path("", view=views.MyProfile1, name="profile"),
    path("shippingaddress/", view=views.ShippingAddress1, name="shippingaddress"),
    path("addshippingaddress/", view=views.AddShippingAddress, name="add-shipping-address"),
    path("my_orders/", view=views.MyOrder, name="my_orders"),
    path("my_review/", view=views.MyReview, name="my_review"),
    path("update_profile/", view=views.UpdateCustomerProfile, name="update_profile"),

]
