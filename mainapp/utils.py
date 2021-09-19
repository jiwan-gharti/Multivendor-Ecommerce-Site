import uuid
from django.shortcuts import get_object_or_404

def image_name_change(instance, filename):
    category_name = instance.category.second_level_category.product_category
    product_name = instance.name
    file_extension = "png"
    image_name = category_name + "/" + product_name + str(uuid.uuid4())[:8] + "." +file_extension
    return image_name

def get_cart_item(pk):
    from mainapp.models import OrderItem
    item = get_object_or_404(OrderItem, pk = pk)
    return item



    


