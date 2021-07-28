from django.db import models
from api.user.models import CustomUser
from api.product.models import Product 

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(
            CustomUser, on_delete=models.CASCADE, null=True, blank=True
            ) #We allow null=True to ease debugging errors. In production you should change this.
    product_names = models.CharField(max_length=500)
    total_products = models.CharField(max_length=500, default=0) #If it defaults to zero, we know there's a bug 
    total_amount = models.CharField(max_length=50, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

