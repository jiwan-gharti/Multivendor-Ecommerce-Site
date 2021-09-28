from .models import OrderItem, ProductCategory, SuperProductCategory

def Category(request):
    navbarcategories     =  SuperProductCategory.objects.filter().distinct()
    # navbarcategories2     =  ProductCategory.objects.filter().distinct()
    if request.user.is_authenticated:
        cart_items_count = OrderItem.objects.filter(user=request.user, ordered = False).count()
    else:
        cart_items_count = '0'

    # print(navbarcategories)
    # print(navbarcategories2)
    return {
        'navbarcategories':navbarcategories,
        'cart_items_count':cart_items_count
        # 'navbarcategories2':navbarcategories2
        }