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

