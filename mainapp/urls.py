from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('details/<int:pk>/',views.details,name='details'),
    path("cart/", views.Cart, name="cart"),
    path("removecart/", views.RemoveCart, name="remove_cart"),
    path('contactus/', views.ContactUs.as_view(),name='contactus'),
    path('aboutus/', views.AboutUs.as_view(),name='aboutus'),
    path('shopping_page/', views.ShoppingPage.as_view(),name='shopping_page'),
    path('shopping_page1/<str:slug>/', views.ShoppingPage1,name='shopping_page1'),
    
    
    path('checkout/', views.CheckoutPage,name='checkout'),
    path('wishlist/', views.WishlistPage.as_view(),name='wishlist'),


    path("update_item/", views.UpdateItem, name= 'update_item'),
    path("payment/", views.PaymentView, name = 'payment'),

    # test 
    # path("test/", views.TestView,name = "test")

]