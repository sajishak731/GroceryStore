from django.db import models

# Create your models here.


class CategoryDb(models.Model):
    category_name = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    category_image =models.ImageField(upload_to="category images",null=True,blank=True)

class ProductDb(models.Model):
    category_name = models.CharField(max_length=100,blank=True,null=True)
    product_name = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    price = models.CharField(max_length=100,blank=True,null=True)
    product_image =models.ImageField(upload_to="product images",null=True,blank=True)





