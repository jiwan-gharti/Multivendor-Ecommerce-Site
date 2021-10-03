from myprofile.models import MerchantReview, MyProfile, ShippingAddress
from django.contrib import admin

# Register your models here.

admin.site.register(ShippingAddress)
admin.site.register(MyProfile)

@admin.register(MerchantReview)
class MerchantRateAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','rate','is_rated','rated_date']
