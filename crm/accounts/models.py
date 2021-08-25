from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=30,blank=True,null=True)
    profile_pic = models.ImageField(default='profile1.png',blank=True,null=True)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=20,blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    category =models.CharField(max_length=20,blank=True,null=True,choices=CATEGORY)
    description =models.TextField(blank=True,null=True)
    data_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out of delivery','Out of delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    data_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,blank=True,null=True,choices=STATUS)
    note = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self) -> str:
        return self.status
