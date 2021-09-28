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
    path('shopping_page/', views.ShoppingPage,name='shopping_page'),
    path('shopping_page1/<str:slug>/', views.ShoppingPage1,name='shopping_page1'),
    # path("load_more_data/", views.LoadMore, name= 'load_more_date'),



    path('merchant_shopping_page/<str:slug>/<int:pk>/', views.ShoppingPage1,name='merchant_shopping_page'),

    path("add_comment/<int:pk>/", views.addComment, name = 'add_comment'),
    path("merchant_list/", views.MerchantList,name = "merchant_list"),
    # path("merchant_shope_page/<int:pk>/", views.MerchantShopPage,name = "merchant_shope_page"),
    
    
    path('checkout/', views.CheckoutPage,name='checkout'),
    path('wishlist_page/', views.WishlistPage1,name='wishlist_page'),
    path('wishlist/<int:pk>/', views.WishlistPage,name='wishlist'),
    path('remove_from_wishlist/<int:pk>/', views.WishlistRemoveItem,name='remove_from_wishlist'),
    path("wishlist_to_cart/",views.WishTocart, name = "wishlist_to_cart"),


    path("update_item/", views.UpdateItem, name= 'update_item'),
    path("payment/", views.PaymentView, name = 'payment'),

    # test 
    # path("test/", views.TestView,name = "test")

    path("post_payment/",views.PostPayment, name="post_payment")

]