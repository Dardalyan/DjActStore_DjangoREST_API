from django.db import models

from model.product.models import Product
from model.user.models import User


# Create your models here.
class Basket(models.Model):
    basket_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='basket')
    products = models.ManyToManyField(Product , related_name='basket')
