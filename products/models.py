from django.db import models
from django.contrib.auth.models import User
# Create your models here.

sizeChoices = [
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
]
colorChoices = [
    ('White', 'White'),
    ('Blue', 'Blue'),
    ('Red', 'Red'),
    ('Yellow', 'Yellow'),
]
class ProductsModel(models.Model) :
    name = models.CharField(max_length = 20,null = True, blank = True)
    size = models.CharField(choices = sizeChoices, max_length =12 , null = True, blank = True)
    color = models.CharField(choices = colorChoices , max_length =12 ,null = True, blank = True)
    image = models.ImageField(upload_to= 'products/images',null = True, blank = True)
    description = models.TextField()
    price = models.DecimalField( decimal_places =2 , max_digits= 12)


 



class reviewModel(models.Model) :
    product = models.ForeignKey(ProductsModel , on_delete = models.CASCADE)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    comment = models.TextField()

class wishlistModel(models.Model) :
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    product = models.ForeignKey(ProductsModel , on_delete = models.CASCADE)
   
