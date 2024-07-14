from django.db import models

# Create your models here.


class Product(models.Model):
    SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
        "XL": "X-Large",
        "XXL":"XX-Large"
    }
    product_id = models.BigAutoField(primary_key=True)
    barcode = models.CharField(max_length=12 , unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    size = models.CharField(max_length=3, choices=SIZES)
    count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='',blank=True, null=True)

    def __str__(self):
        return str({
            'product_id': self.product_id,
            'barcode': self.barcode,
            'name': self.name,
            'price': self.price,
            'size': self.size,
            'count': self.count,
            'image': self.image
        })


