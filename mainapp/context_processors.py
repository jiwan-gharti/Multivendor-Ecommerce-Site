from .models import ProductCategory, SuperProductCategory

def Category(request):
    navbarcategories     =  SuperProductCategory.objects.filter().distinct()
    # navbarcategories2     =  ProductCategory.objects.filter().distinct()

    # print(navbarcategories)
    # print(navbarcategories2)
    return {
        'navbarcategories':navbarcategories,
        # 'navbarcategories2':navbarcategories2
        }