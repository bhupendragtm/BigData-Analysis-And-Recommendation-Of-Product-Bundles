from django.db import models
from jsonfield import JSONField

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200,blank=True,null=True)
    province = models.CharField(max_length=200,blank=True,null=True)
    zipcode= models.CharField(max_length=200,blank=True,null=True)
    date = models.DateField(auto_now_add=True)


class Product(models.Model):
    # order = models.ForeignKey(Order,on_delete=models.CASCADE) #one order can have many items
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name="product")
    product_D = models.TextField()
    total = models.CharField(max_length =200)

