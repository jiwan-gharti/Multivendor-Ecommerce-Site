from accounts.models import User
from mainapp.models import Discount, OrderItem, Product, ProductAlternativeImage, ProductCategory, ProductInventory
from django.shortcuts import redirect, render
from .forms import MerchantProfileForm, ProductForm,DiscountForm,ProductInventoryForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


@login_required
def MerchantDashbord(request):
    if request.user.is_merchant:       
        ProductForm1 = ProductForm()
        DiscountForm1 = DiscountForm(prefix="discount")
        ProductInventoryForm1 = ProductInventoryForm()

        if request.method == "POST":
            ProductForm1 = ProductForm(data = request.POST or None,files=request.FILES)
            DiscountForm1 = DiscountForm(request.POST, prefix="discount")
            ProductInventoryForm1 = ProductInventoryForm(request.POST or None)

            

            if ProductForm1.is_valid()  and DiscountForm1.is_valid() and ProductInventoryForm1.is_valid():
            
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

                
                
                category_obj = ProductCategory.objects.get(brand_name = brand_name)
                print("objects---------",category_obj)

                discount_obj = Discount.objects.create(name = discount_name, description=discount_description,active=active,discount_percentage=discount_percentage)
                inventory_obj = ProductInventory.objects.create(quantity=quantity)

                

                data = Product.objects.create(
                    user = request.user,
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

                images = request.FILES.getlist("images")
                print("----------FILES-------",images)

                for image in images:
                    product_sub_image_obj = ProductAlternativeImage.objects.create(
                                    alternative_image = image,
                                    product = data                                    
                                    )
                
                    product_sub_image_obj.save()

                messages.success(request,"Your Product is Added !!")
                print("saved!!!")
            else:
                print("else part")
        
        
        #for mProfile
        
        


        all_products = Product.objects.filter(user = request.user)

        merchant_user = User.objects.get(id = request.user.pk)
        print(merchant_user)


        low_stock = all_products.filter(inventory__quantity__lte = 5).count()
        print(low_stock)

        my_orders = OrderItem.objects.filter(item__user=merchant_user, ordered = True)
        # print(my_orders)
        total_sell = 0
        for order in my_orders:
            total_sell += float(order.get_total_price)


        context = {
            'ProductForm1':ProductForm1,
            'DiscountForm1':DiscountForm1,
            'ProductInventoryForm1':ProductInventoryForm1,
            'all_products':all_products,
            'merchant_user':merchant_user,
            'low_stock':low_stock,
            'my_orders':my_orders,
            'total_sell':total_sell

        }
        return render(request, 'merchant/merchant_home_page.html', context)
    else:
            messages.info(request, "Access Denied! Login as a Merchant.")
            return redirect("/")



@login_required
def DeleteProduct(request,pk):
    if request.user.is_merchant:
        print("HERE!!!")
        delete_product  = Product.objects.get(pk = pk)
        delete_product.delete()
        return redirect("/merchant/")
    else:
            messages.info(request, "Access Denied! Login as a Merchant.")
            return redirect("/")

@login_required
def UpdateProduct(request,pk):
    if request.user.is_merchant:
        update_product  = Product.objects.get(pk = pk)
        ProductForm1 = ProductForm(instance = update_product)

        inventory_obj = ProductInventory.objects.all()
        single_inventory_obj = inventory_obj.get(inventory__id = pk)
        ProductInventoryForm1 = ProductInventoryForm(instance=single_inventory_obj)

        
        discount_obj = Discount.objects.all()
        if update_product.discount and update_product.discount.active:
            single_discount_obj = discount_obj.get(discount__id = pk)
            DiscountForm1 = DiscountForm(prefix="discount",instance=single_discount_obj)
        else:
            DiscountForm1 = DiscountForm(prefix="discount")
        print(single_inventory_obj)
      

        if request.method == "POST":
            ProductForm1 = ProductForm(request.POST,request.FILES,instance = update_product)
            if update_product.discount and update_product.discount.active:
                single_discount_obj = discount_obj.get(discount__id = pk)
                DiscountForm1 = DiscountForm(prefix="discount",data = request.POST,instance=single_discount_obj)  
            else:
                single_discount_obj = discount_obj.get(discount__id = pk)
                DiscountForm1 = DiscountForm(prefix="discount",data = request.POST)    
                
            ProductInventoryForm1 = ProductInventoryForm(request.POST, instance=single_inventory_obj)

            if ProductForm1.is_valid() and DiscountForm1.is_valid() and ProductInventoryForm1.is_valid():
                ProductForm1.save()
                DiscountForm1.save()
                ProductInventoryForm1.save()
                return redirect("/merchant/")
            else:
                print("form invalid!!")
        

        context = {
            'ProductForm1':ProductForm1,
            'DiscountForm1':DiscountForm1,
            'ProductInventoryForm1':ProductInventoryForm1,

        }

        return render(request,'merchant/mUpdateProduct.html',context)
    else:
            messages.info(request, "Access Denied! Login as a Merchant.")
            return redirect("/")

@login_required
def mProfileUpdate(request):
    if requset.user.is_merchant:
    # merchant_user = User.objects.get(pk = pk)
        mProfileUpdateForm = MerchantProfileForm(instance = request.user)

        if request.method == "POST":
            mProfileUpdate = MerchantProfileForm(request.POST, request.FILES, instance=request.user)
            if mProfileUpdate.is_valid():
                mProfileUpdate.save()
                return redirect("/merchant/")

        context = {
            'mProfileUpdateForm':mProfileUpdateForm
        }
        return render(request, 'merchant/mUpdateProfile.html',context)
    else:
            messages.info(request, "Access Denied! Login as a Merchant.")
            return redirect("/")


def Logout(request):
    logout(request)
    return redirect("accounts:login")




def API_data(request):
    data = {
        'customer': 30,
        'price' : 10
    }
    return JsonResponse(data)
