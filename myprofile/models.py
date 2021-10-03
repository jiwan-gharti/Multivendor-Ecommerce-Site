from django.db import models
from django.db.models.aggregates import Avg
from accounts.models import User
from phonenumber_field.modelfields import PhoneNumberField
from mainapp.models import OrderItem

# Create your models here.
SHIPPING_ADDRESS = (
    ('Office', 'Office'),
    ('Home', 'Home'),
)

class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=100)
    receiver_no = PhoneNumberField(region="NP")
    region = models.CharField(max_length=100)
    city   = models.CharField(max_length=100)
    area   = models.CharField(max_length=100)
    address = models.CharField(max_length=100, help_text="House# 001")
    label   = models.CharField(max_length=8, choices=SHIPPING_ADDRESS)

    class Meta:
        verbose_name = "Customer Shipping Address"
        verbose_name_plural = "Customer Shipping Address"

    
    def __str__(self):
        return f'{self.full_name}-{self.area}'

class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    mobile = PhoneNumberField(region="NP")

    class Meta:
        verbose_name = "Customer Profile"
        verbose_name_plural = "Customer Profile"

    def __str__(self):
        return str(self.user.username)
    

class MerchantReview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(OrderItem,on_delete = models.CASCADE, null= True)
    rate = models.IntegerField()
    is_rated = models.BooleanField(default=False)
    rated_date = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return str(self.rate)

    # @property
    # def get_average_merchant_rating(self):
    #     print(self)
    #     # merchants = MerchantReview.objects.filter(self)
    #     # average_merchant_rating = merchants.aggregate(Avg("rate"))
    #     # print(average_merchant_rating)
    #     # return average_merchant_rating