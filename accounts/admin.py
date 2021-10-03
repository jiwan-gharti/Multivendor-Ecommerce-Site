from django.contrib import admin
# from .models import MerchantUser
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','first_name','last_name','email','phone_number','address','gender','is_superuser','is_customer','is_merchant','pan_no','document')

