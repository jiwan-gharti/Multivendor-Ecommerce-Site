from mainapp.models import Discount, Product, ProductCategory, ProductInventory, SecondLevelCategory, SuperProductCategory
from django.shortcuts import render
from .forms import ProductForm,ProductCategoryForm,SecondLevelCategoryForm,DiscountForm,ProductInventoryForm

def MerchantDashbord(request):
       
    ProductForm1 = ProductForm()
    ProductCategoryForm1= ProductCategoryForm()
    SecondLevelCategoryForm1 = SecondLevelCategoryForm()
    DiscountForm1 = DiscountForm()
    ProductInventoryForm1 = ProductInventoryForm()

    if request.method == "POST":
        ProductForm1 = ProductForm(request.POST or None)
        ProductCategoryForm1= ProductCategoryForm(request.POST or None)
        SecondLevelCategoryForm1 = SecondLevelCategoryForm(request.POST or None)
        DiscountForm1 = DiscountForm(request.POST or None)
        ProductInventoryForm1 = ProductInventoryForm(request.POST or None)

        # first_level_category = SecondLevelCategoryForm1['first_level_category']
        # print(first_level_category)
        # print(type(first_level_category))
        print("outer ")

        if (ProductForm1.is_valid() and ProductCategoryForm1.is_valid() and SecondLevelCategoryForm1.is_valid() and DiscountForm1.is_valid() and ProductInventoryForm1.is_valid()):
            print("POST request got")
            ProductForm1.save(commit=False)

            # product model fields
            product_image = ProductForm1.cleaned_data['image']
            product_name = ProductForm1.cleaned_data['name']
            product_description = ProductForm1.cleaned_data['description']
            product_price = ProductForm1.cleaned_data['price']
            availability = ProductForm1.cleaned_data['availability']

            #category
            first_level_category = ProductCategoryForm1.cleaned_data['first_level_category']
            brand_name = ProductCategoryForm1.cleaned_data['brand_name']

            #secondary
            second_level_category = SecondLevelCategoryForm1.cleaned_data['second_level_category']
            
            #discount
            discount_name = DiscountForm1.cleaned_data['discount_name']
            discount_description = DiscountForm1.cleaned_data['discount_description']
            active = DiscountForm1.cleaned_data['active']
            discount_percentage = DiscountForm1.cleaned_data['discount_percentage']

            quantity = ProductInventoryForm1.cleaned_data['quantity']

            
            first_level_category_object = SuperProductCategory.objects.create(first_level_category = first_level_category)
            second_level_category_object = SecondLevelCategory.objects.create(first_level_category = first_level_category_object)
            category_obj = ProductCategory.objects.create(second_level_category=second_level_category_object, brand_name = brand_name)
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
            print("saved!!!")
        else:
            print(ProductForm1,ProductCategoryForm1)


        

    context = {
        'ProductForm1':ProductForm1,
        'ProductCategoryForm1':ProductCategoryForm1,
        'SecondLevelCategoryForm1':SecondLevelCategoryForm1,
        'DiscountForm1':DiscountForm1,
        'ProductInventoryForm1':ProductInventoryForm1

    }
    return render(request, 'merchant/merchant_home_page.html', context)
