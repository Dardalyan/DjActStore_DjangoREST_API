from django.db import models
from model.user.models import User


# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    country = models.CharField(max_length=128,null=False,blank=False)
    city = models.CharField(max_length=128,null=False,blank=False)
    province = models.CharField(max_length=128, null=False,blank=False)
    neighborhood = models.CharField(max_length=128,null=False,blank=False)
    address = models.CharField(max_length=255, null=False,blank=False)

    def __str__(self):
        return str({
            'user': self.user,
            'country': self.country,
            'city': self.city,
            'province': self.province,
            'neighborhood': self.neighborhood,
            'address': self.address,
        })