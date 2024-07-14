from django.db import models
from model.user.models import User


from model.product.models import Product


# Create your models here.
class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    products = models.ManyToManyField(Product ,related_name='order')
