from django.db import models
from django.db.models.aggregates import Avg
from .utils import image_name_change
from django.template.defaultfilters import slugify

from accounts.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from .managers import OrderItemManager



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
                                                unique=True,
                                                 help_text="Like Electronic or Beauty Products or Sport and OutDoors",
                                                )

    class Meta:
        verbose_name = "First Level Category"
        verbose_name_plural = "First Level Categories"

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
    product_category         =     models.CharField("Product Category Name (2nd level)",max_length=200, unique=True)
    first_level_category     =     models.ForeignKey(SuperProductCategory, on_delete=models.CASCADE)
    slug                =       models.SlugField(max_length=300,blank=True,null=True)
      

    class Meta:
        verbose_name = "Second Level Category"
        verbose_name_plural = "Second Level Categories"

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
    brand_name                =     models.CharField("Brand Name",max_length=200)
    description               =     models.CharField(max_length=2000,null=True, blank= True)
    slug                =           models.SlugField(max_length=300,blank=True,null=True)


    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
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
    quantity             =     models.IntegerField(default=1)

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
    user                   =     models.ForeignKey(User,on_delete=models.CASCADE)
    image                  =     models.ImageField("Product Image",upload_to = image_name_change)
    name                   =     models.CharField("Product Name",max_length=120)
    small_description      =     models.TextField(max_length = 500)
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
    
    @property
    def get_average_rating(self):
        average_rating = Comment.objects.filter(product = self).aggregate(rating_avg=Avg("rate"))
        return average_rating
    
    

class ProductAlternativeImage(models.Model):
    alternative_image = models.ImageField(upload_to = "alternative Images")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.name) + " Sub-Image"



class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    item = models.ForeignKey(Product, on_delete=models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'ShippingAddress', related_name='shipping_address', on_delete=models.SET_NULL,blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL,blank=True, null=True)
    
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

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

    
    object = objects = models.Manager() # The default manager.
    order_items = OrderItemManager()


    


        
    

    

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
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # order_item = models.ForeignKey(OrderItem, on_delete=models.SET_NULL,null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models. CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    country = CountryField(multiple=False)
    city_address = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    zip = models.CharField(max_length=100,null=True, blank=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    payment_option = models.CharField(max_length=2)

    def __str__(self):
        return str(self.city_address) +" , "+ str(self.street_address)

    class Meta:
        verbose_name_plural = 'Shipping Addresses'
        ordering = ('-ordered_date',)



COMMENT_CHOICE = [
    ('Best','Best'),
    ('Average','Average'),
    ('Poor','Poor'),
]
class Comment(models.Model):
    STATUS = [
        ('New','New'),
        ('True', 'True'),
        ('False',"False")
    ]
    product    = models.ForeignKey(Product,on_delete= models.CASCADE)
    user       = models.ForeignKey(User,on_delete= models.CASCADE)
    subject    = models.CharField(max_length=50, blank=True, choices=COMMENT_CHOICE, default="Best")
    comment    = models.CharField(max_length=200, blank=True)
    rate       = models.SmallIntegerField(default = 1)
    ip         = models.CharField(max_length=20, blank=True)
    sentiment  = models.CharField(max_length=5, null=True ,blank= True)
    status     = models.CharField(max_length=10, choices=STATUS,default="New")
    created    =    models.DateTimeField(auto_now_add=True)
    updated    =    models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject + "-title"
    
    
    
    
    




class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ContactUS(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(region='NP')
    message = models.TextField()

    def __str__(self):
        return self.name


    
    


