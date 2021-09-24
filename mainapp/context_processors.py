from .models import OrderItem, ProductCategory, SuperProductCategory

def Category(request):
    navbarcategories     =  SuperProductCategory.objects.filter().distinct()
    # navbarcategories2     =  ProductCategory.objects.filter().distinct()
    cart_items_count = OrderItem.objects.all().count()

    # print(navbarcategories)
    # print(navbarcategories2)
    return {
        'navbarcategories':navbarcategories,
        'cart_items_count':cart_items_count
        # 'navbarcategories2':navbarcategories2
        }