from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('details/',views.details,name='details'),
    path('cart/', views.CartTemplate.as_view(),name='cart'),
    path('contactus/', views.ContactUs.as_view(),name='contactus'),
    path('aboutus/', views.AboutUs.as_view(),name='aboutus'),
    path('shopping_Page/', views.ShoppingPage.as_view(),name='shopping_page'),
    path('checkout/', views.CheckoutPage.as_view(),name='checkout'),

]