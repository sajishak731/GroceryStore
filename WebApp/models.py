from django.db import models

# Create your models here.

class ContactDb(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    email =models.CharField(max_length=100,blank=True,null=True)
    subject = models.CharField(max_length=100,blank=True,null=True)
    message =models.CharField(max_length=100,blank=True,null=True)

class RegistrationDb(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password =models.CharField(max_length=100, blank=True, null=True)
    confirm_password =models.CharField(max_length=100, blank=True, null=True)

class CartDb(models.Model):
    UserName=models.CharField(max_length=100,blank=True,null=True)
    Product_Name=models.CharField(max_length=100,blank=True,null=True)
    Quantity=models.IntegerField(blank=True,null=True)
    Price=models.IntegerField(blank=True,null=True)
    Total_Price=models.IntegerField(blank=True,null=True)
    Product_Img=models.ImageField(upload_to="cart images",null=True,blank=True)