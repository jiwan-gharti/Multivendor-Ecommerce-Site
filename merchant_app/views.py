from mainapp.models import Discount, Product, ProductCategory, ProductInventory, SecondLevelCategory, SuperProductCategory
from django.shortcuts import render
from .forms import ProductForm,ProductCategoryForm,SecondLevelCategoryForm,DiscountForm,ProductInventoryForm
from django.contrib import messages
from django.http import JsonResponse

def MerchantDashbord(request):
       
    ProductForm1 = ProductForm()
    ProductCategoryForm1= ProductCategoryForm()
    SecondLevelCategoryForm1 = SecondLevelCategoryForm()
    DiscountForm1 = DiscountForm(prefix="discount")
    ProductInventoryForm1 = ProductInventoryForm()

    if request.method == "POST":
        ProductForm1 = ProductForm(data = request.POST or None,files=request.FILES)
        ProductCategoryForm1= ProductCategoryForm(request.POST or None)
        SecondLevelCategoryForm1 = SecondLevelCategoryForm(request.POST or None)
        DiscountForm1 = DiscountForm(request.POST, prefix="discount")
        ProductInventoryForm1 = ProductInventoryForm(request.POST or None)

        

        if ProductForm1.is_valid() and ProductCategoryForm1.is_valid() and SecondLevelCategoryForm1.is_valid() and DiscountForm1.is_valid() and ProductInventoryForm1.is_valid():
        
            # print(ProductForm1)
            print("POST request got")
            ProductForm1.save(commit=False)

            # product model fields
            product_image = ProductForm1.cleaned_data.get('image',"default")
            print("product-image",product_image)
            product_name = ProductForm1.cleaned_data.get('name')
            print(product_name)
            product_description = ProductForm1.cleaned_data.get('description')
            print(product_description)
            product_price = ProductForm1.cleaned_data.get('price')
            print(product_price)
            availability = ProductForm1.cleaned_data.get('availability')
            print(availability)
            brand_name = ProductForm1.cleaned_data.get('category')
            print("category-------------",brand_name)

            #category
            second_level_category = ProductCategoryForm1.cleaned_data.get('second_level_category')
            print(second_level_category)
            
            #secondary
            first_level_category = SecondLevelCategoryForm1.cleaned_data.get('first_level_category')
            print(first_level_category)
            #discount
            discount_name = DiscountForm1.cleaned_data.get('name')
            print(discount_name)
            discount_percentage = DiscountForm1.cleaned_data.get('discount_percentage') 
            active = DiscountForm1.cleaned_data.get('active')
            print(active)
            discount_description = DiscountForm1.cleaned_data.get('description')
            print(discount_description)

            quantity = ProductInventoryForm1.cleaned_data.get('quantity')
            print(quantity)

            
            # first_level_category_obj = SuperProductCategory.objects.get(first_level_category = first_level_category)
            # print("object",first_level_category)

            # second_level_category_obj = SecondLevelCategory.objects.get(product_category = second_level_category)
            # print("objects",second_level_category)
            category_obj = ProductCategory.objects.get(brand_name = brand_name)
            print("objects---------",category_obj)

            discount_obj = Discount.objects.create(name = discount_name, description=discount_description,active=active,discount_percentage=discount_percentage)
            inventory_obj = ProductInventory.objects.create(quantity=quantity)

            

            data = Product.objects.create(
                image = product_image,
                name = product_name,
                description = product_description,
                price = product_price,
                availability = availability,
                category = category_obj,
                discount=discount_obj,
                inventory = inventory_obj,
            
            )
            data.save()
            messages.success(request,"Your Product is Added !!")
            print("saved!!!")
        else:
            print("else part")
            



        

    context = {
        'ProductForm1':ProductForm1,
        'ProductCategoryForm1':ProductCategoryForm1,
        'SecondLevelCategoryForm1':SecondLevelCategoryForm1,
        'DiscountForm1':DiscountForm1,
        'ProductInventoryForm1':ProductInventoryForm1

    }
    return render(request, 'merchant/merchant_home_page.html', context)

def API_data(request):
    data = {
        'customer': 30,
        'price' : 10
    }
    return JsonResponse(data)
