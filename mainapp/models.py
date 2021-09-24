from django.db import models
from .utils import image_name_change
from django.template.defaultfilters import slugify

from accounts.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField



# Create your models here.

class ProductBaseClass(models.Model):
    created               =    models.DateTimeField(auto_now_add=True)
    updated               =    models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class FeaturedSlider(ProductBaseClass):
    name                =      models.CharField(max_length=100)
    description         =      models.CharField(max_length=400)
    slug                =      models.SlugField(max_length=300,blank=True,null=True)
    image               =      models.ImageField(upload_to = 'featuresImages/')
    active              =      models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class SuperProductCategory(models.Model):
    first_level_category     =     models.CharField(max_length=100,
                                                blank=True, null=True,
                                                unique=True,
                                                 help_text="Like Electronic or Beauty Products or Sport and OutDoors",
                                                )
    def __str__(self):
        return str(self.first_level_category)

    def save(self,*args, **kwargs):
        self.general_category = self.first_level_category.lower()
        super().save(*args, **kwargs)
    
    def secondLevelItems(self):
        firstLevelItem = SuperProductCategory.objects.get(id = self.id)
        # print(firstLevelItem)
        SecondLevelItems = SecondLevelCategory.objects.filter(first_level_category = firstLevelItem)
        # print(SecondLevelItems)
        # print("here")
        return SecondLevelItems
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.first_level_category)
        super().save(*args, **kwargs)

    
class SecondLevelCategory(models.Model):
    product_category         =     models.CharField("Product Category Name (2nd level)",max_length=200, blank= True, null=True)
    first_level_category     =     models.ForeignKey(SuperProductCategory, on_delete=models.CASCADE)
    slug                =       models.SlugField(max_length=300,blank=True,null=True)
      

    def __str__(self):
        return str(self.product_category)
    
    def save(self,*args, **kwargs):
        self.product_category = self.product_category.lower()
        self.slug = slugify(self.product_category)
        super().save(*args, **kwargs)

    def thirdLevelItems(self):
        # print(self.pk)
        secondLevelItem = SecondLevelCategory.objects.get(pk = self.pk)
        # print(secondLevelItem)
        thirdLevelItems = ProductCategory.objects.filter(second_level_category = secondLevelItem)
        # print(thirdLevelItems)
        return thirdLevelItems
            


    

class ProductCategory(ProductBaseClass):

    second_level_category     =     models.ForeignKey(SecondLevelCategory, on_delete=models.CASCADE)
    brand_name                =     models.CharField("Brand Name",max_length=200, null=True, blank= True)
    description               =     models.CharField(max_length=2000)
    slug                =           models.SlugField(max_length=300,blank=True,null=True)



    class Meta:
        verbose_name          =    "Product Category"
        verbose_name_plural   =    "Product Categories"
        db_table              =    "Product Category"

    def __str__(self):
        return str(self.brand_name)


 
    def save(self,*args, **kwargs):
        self.brand_name = self.brand_name.lower()
        self.slug = slugify(self.brand_name)
        super().save(*args, **kwargs)



class ProductInventory(ProductBaseClass):
    quantity             =     models.IntegerField(default=1,null=True, blank=True)

    class Meta:
        verbose_name        =   "Product Inventory"
        verbose_name_plural =   "Product Inventories"
        db_table            =   "Product Inventory"
    
    def __str__(self):
            return str(self.quantity)

class Discount(ProductBaseClass):
    name                 =     models.CharField("Discount Name",max_length=200,null=True, blank=True)
    description          =     models.CharField(max_length=200,null=True, blank=True)
    active               =     models.BooleanField(default=False,)
    discount_percentage  =     models.DecimalField(max_digits=4, decimal_places=2,null=True, blank=True)
    slug                =      models.SlugField(max_length=300,blank=True,null=True)

    class Meta:
        db_table = "Product Discount"
    
    def save(self,*args, **kwargs):
        # self.brand_name = self.brand_name.lower()
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
            return str(self.name)

class Product(ProductBaseClass):
    user                   =     models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank = True)
    image                  =     models.ImageField("Product Image",upload_to = image_name_change, null=True, blank = True)
    name                   =     models.CharField("Product Name",max_length=120)
    description            =     models.CharField("Product Description",max_length=2000)
    price                  =     models.DecimalField("Price",max_digits=8, decimal_places=2, help_text="Price should Grater than 20")
    availability           =     models.BooleanField(default=True)
    category               =     models.ForeignKey(ProductCategory, models.CASCADE, null=True, blank = True)
    inventory              =     models.ForeignKey(ProductInventory, models.CASCADE, null=True, blank = True, verbose_name="Quantity", related_query_name="inventory")
    discount               =     models.ForeignKey(Discount, models.CASCADE, null=True, blank = True,related_query_name="discount")
    slug                   =      models.SlugField(max_length=300,blank=True,null=True)

    class Meta:
        db_table            =   "Product"
        constraints         =   [models.CheckConstraint(check= models.Q(price__gt = 20), name="price Constraints")]

    def __str__(self):
            return str(self.name)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def calculate_Discount(self):
        obj = Product.objects.get(pk = self.pk)
        discount_per = obj.discount.discount_percentage
        # print(obj.discount.discount_percentage)
        value = float(self.price - (self.price* discount_per * 1 / 100))
        return "%.2f"%value
    
    @property
    def get_discount_status(self):
        return self.discount.discount_percentage
    

class ProductAlternativeImage(models.Model):
    alternative_image = models.ImageField(upload_to = "alternative Images")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.name) + " Sub-Image"



class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=False , blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False,null=True, blank=True)

    def __str__(self):
        return str(self.item.name)
    
    @property
    def get_total_price(self):
        if self.item.discount and self.item.discount.active:
            price = self.item.calculate_Discount
            item_total = float(price)* self.quantity
            return item_total
        else:
            item_total = float(self.item.price) * self.quantity
            return item_total
    
    @property
    def get_cart_total(cls):
        total = 0
        
        for item in OrderItem.objects.all():
            total += item.get_total_price
        return total
    
    def total_cart_items(self):
        return OrderItem.objects.all().count()


        
    

    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    item = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True, blank=True)
    ordered = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.

    
    # def get_cart_total(self):
    #     total = 0
        
    #     for items in self.item.all():
    #         total += items.get_total_price()
    #     return total


class ShippingAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    # order_item = models.ForeignKey(OrderItem, on_delete=models.SET_NULL,null=True, blank=True)
    first_name = models.CharField(max_length=30,null=True, blank=True)
    last_name = models. CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    country = CountryField(multiple=False, null=True, blank=True)
    city_address = models.CharField(max_length=100,null=True, blank=True)
    street_address = models.CharField(max_length=100,null=True, blank=True)
    zip = models.CharField(max_length=100,null=True, blank=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    payment_option = models.CharField(max_length=2, null=True, blank=True)
    # default = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name_plural = 'Shipping Addresses'



class Comment(models.Model):
    STATUS = [
        ('New','New'),
        ('True', 'True'),
        ('False',"False")
    ]
    product    = models.ForeignKey(Product,on_delete= models.CASCADE)
    user       = models.ForeignKey(User,on_delete= models.CASCADE)
    subject    = models.CharField(max_length=50, blank=True)
    comment    = models.CharField(max_length=200, blank=True)
    rate       = models.SmallIntegerField(default = 1)
    ip         = models.CharField(max_length=20, blank=True)
    status     = models.CharField(max_length=10, choices=STATUS,default="New")
    created    =    models.DateTimeField(auto_now_add=True)
    updated    =    models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject + "-title"


