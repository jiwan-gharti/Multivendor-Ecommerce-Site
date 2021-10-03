from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg
from phonenumber_field.modelfields import PhoneNumberField

# from myprofile.models import MerchantReview
# Create your models here.

class User(AbstractUser):
    gender = [
        ("Male", 'Male'),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    phone_number = PhoneNumberField(region="NP")
    shop_name   = models.CharField(max_length=40)
    address      = models.CharField(max_length=200,null=True)
    gender       = models.CharField(max_length=6, choices=gender)
    is_customer  = models.BooleanField(default=False)
    is_merchant  = models.BooleanField(default=False)
    pan_no       = models.BigIntegerField("User Pan Number", unique=True, null=True)
    document     = models.ImageField(upload_to="merchant documents")


    def __str__(self):
        return self.username
    
    @property
    def get_average_merchant_rating(self):
        print(self)
        from myprofile.models import MerchantReview
        merchants = MerchantReview.objects.filter(user=self)
        average_merchant_rating = merchants.aggregate(Avg("rate"))
        print(average_merchant_rating)
        return average_merchant_rating





    # def __str__(self):
    #     return str(self.pan_no)


