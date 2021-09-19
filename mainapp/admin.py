from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductInventory)
admin.site.register(SuperProductCategory)
admin.site.register(Discount)
admin.site.register(SecondLevelCategory)
admin.site.register(FeaturedSlider)


admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
# admin.site.register(Order)

# admin.site.register(Order)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['image','name','description','price','availability','category','inventory','discount']


# @admin.register(ProductCategory)
# class ProductCategoryAdmin(admin.ModelAdmin):
#     list_display = ['general_category','product_category','brand_name','description']


# @admin.register(ProductInventory)
# class ProductInventoryAdmin(admin.ModelAdmin):
#     list_display = ['quantity']


# @admin.register(Discount)
# class DiscountAdmin(admin.ModelAdmin):
#     list_display = ['name','description','active','discount_percentage']