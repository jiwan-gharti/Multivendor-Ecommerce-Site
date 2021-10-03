from django.contrib import admin
from .models import *

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('description','small_description')
    exclude = ('slug',)
    list_display = ['id','user','image','name','price','availability','category','inventory','discount']

    fieldsets = (
        ('Products Info', {
            'fields': ('name','user', 'image','price','availability','category','inventory')
        }),
        ('Discount', {
            'classes': ('collapse',),
            'fields': ('discount',),
        }),
    )


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    list_display = ['id','brand_name','second_level_category']


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ['id','quantity']



@admin.register(SecondLevelCategory)
class SecondLevelCategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ['id','product_category','first_level_category']


@admin.register(SuperProductCategory)
class SuperProductCategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ['id','first_level_category',]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ['id','name','description','active','discount_percentage']



@admin.register(FeaturedSlider)
class FeaturedSliderAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ['id','name','image','active','description']



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id','user','item','quantity','shipping_address','payment','ordered','being_delivered','received']


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','email','phone_number','country','city_address','street_address','zip','payment_option','ordered_date']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','product','user','subject','comment','rate','sentiment','ip','status','created']


@admin.register(ProductAlternativeImage)
class ProductAlternativeImageAdmin(admin.ModelAdmin):
    list_display = ['id','product','alternative_image']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id','stripe_charge_id','user','amount','timestamp']

@admin.register(ContactUS)
class  ConatactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_number','message']