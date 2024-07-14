#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import django
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile

from DjActStore.settings import BASE_DIR

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjActStore.settings")
django.setup()


from model.product.models import Product
from model.user.models import User
from model.address.models import Address
from model.basket.models import Basket


def createUsers():
    """Creates users."""
    User.objects.all().delete()

    User.objects.create_user('5894567321','+1','US','123456',name="John",surname="Butler",age=21)
    User.objects.create_user('5378976145','+1','US','123456',name="Nicole",surname="Brown",age=32)
    User.objects.create_user('5316547898','+1','US','123456',name="Yumi",surname="Sky",age=55)
    User.objects.create_user('5213246785','+1','US','123456',name="Harold",surname="Broadway",age=41)
    User.objects.create_user('5322899876','+1','US','123456',name="James",surname="Fisher",age=36)


def createProducts():
    """Creates products."""
    Product.objects.all().delete()
    Product.objects.create(barcode=823543768540,name='Black T-Shirt',price=29.0,size='S',count=10,image="")
    Product.objects.create(barcode=823543768550,name='Black T-Shirt',price=29.0,size='M',count=10,image="")
    Product.objects.create(barcode=823543768560,name='Black T-Shirt',price=29.0,size='L',count=10,image="")
    Product.objects.create(barcode=823543768570,name='Black T-Shirt',price=29.0,size='XL',count=10,image="")
    Product.objects.create(barcode=823543768580,name='Black T-Shirt',price=29.0,size='XXL',count=10,image="")
    Product.objects.create(barcode=874628436530,name='White T-Shirt',price=25.0,size='S',count=10,image="")
    Product.objects.create(barcode=874628436540,name='White T-Shirt',price=25.0,size='M',count=10,image="")
    Product.objects.create(barcode=874628436550,name='White T-Shirt',price=25.0,size='L',count=10,image="")
    Product.objects.create(barcode=874628436560,name='White T-Shirt',price=25.0,size='XL',count=10,image="")
    Product.objects.create(barcode=874628436570,name='White T-Shirt',price=25.0,size='XXL',count=10,image="")
    Product.objects.create(barcode=876452826450,name='Red T-Shirt',price=24.0,size='S',count=10,image="")
    Product.objects.create(barcode=876452826460,name='Red T-Shirt',price=24.0,size='M',count=10,image="")
    Product.objects.create(barcode=876452826470,name='Red T-Shirt',price=24.0,size='L',count=10,image="")
    Product.objects.create(barcode=876452826480,name='Red T-Shirt',price=24.0,size='XL',count=10,image="")
    Product.objects.create(barcode=876452826490,name='Red T-Shirt',price=24.0,size='XXL',count=10,image="")
    Product.objects.create(barcode=819374534830,name='Blue T-Shirt',price=28.0,size='S',count=10,image="")
    Product.objects.create(barcode=819374534840,name='Blue T-Shirt',price=28.0,size='M',count=10,image="")
    Product.objects.create(barcode=819374534850,name='Blue T-Shirt',price=28.0,size='L',count=10,image="")
    Product.objects.create(barcode=819374534860,name='Blue T-Shirt',price=28.0,size='XL',count=10,image="")
    Product.objects.create(barcode=819374534870,name='Blue T-Shirt',price=28.0,size='XXL',count=10,image="")
    Product.objects.create(barcode=867592637840,name='Black Sweat Pant',price=37.0,size='S',count=10,image="")
    Product.objects.create(barcode=867592637850,name='Black Sweat Pant',price=37.0,size='M',count=10,image="")
    Product.objects.create(barcode=867592637860,name='Black Sweat Pant',price=37.0,size='L',count=10,image="")
    Product.objects.create(barcode=867592637870,name='Black Sweat Pant',price=37.0,size='XL',count=10,image="")
    Product.objects.create(barcode=867592637880,name='Black Sweat Pant',price=37.0,size='XXL',count=10,image="")
    Product.objects.create(barcode=854721428310,name='White Sweat Pant',price=35.0,size='S',count=10,image="")
    Product.objects.create(barcode=854721428320,name='White Sweat Pant',price=35.0,size='M',count=10,image="")
    Product.objects.create(barcode=854721428330,name='White Sweat Pant',price=35.0,size='L',count=10,image="")
    Product.objects.create(barcode=854721428340,name='White Sweat Pant',price=35.0,size='XL',count=10,image="")
    Product.objects.create(barcode=854721428350,name='White Sweat Pant',price=35.0,size='XXL',count=10,image="")
    Product.objects.create(barcode=865372694040,name='Green Sweat Pant',price=41.0,size='S',count=10,image="")
    Product.objects.create(barcode=865372694050,name='Green Sweat Pant',price=41.0,size='M',count=10,image="")
    Product.objects.create(barcode=865372694060,name='Green Sweat Pant',price=41.0,size='L',count=10,image="")
    Product.objects.create(barcode=865372694070,name='Green Sweat Pant',price=41.0,size='Xl',count=10,image="")
    Product.objects.create(barcode=865372694080,name='Green Sweat Pant',price=41.0,size='XXl',count=10,image="")


def createAddresses():
    """Creates just one address for each user initially."""
    Address.objects.all().delete()
    for i in range (21,26):
        user = User.objects.get(id=i)
        if i == 21:
            Address.objects.create(user=user,country='United States',city = 'Port Lenoratown',province='New Mexico',neighborhood='McKenzie Branch',address= '74626 Alexandre Tunnel Building Number : 64553')#country, city, province, neighbourhood, address
        if i == 22:
            Address.objects.create(user=user,country='United States',city = 'West Genesisland',province='Kansas',neighborhood='Angie Row',address= '4727 Mueller Spurs Apt. 460 Building Number : 3521')#country, city, province, neighbourhood, address
        if i == 23:
            Address.objects.create(user=user,country='United States',city = 'Lucioshire',province='North Carolina',neighborhood='Minerva Track',address= '304 Schmeler Greens Apt. 948 Building Number : 8495')#country, city, province, neighbourhood, address
        if i == 24:
            Address.objects.create(user=user,country='United States',city = 'Oranbury',province='Tennessee',neighborhood='Stephany View',address= '6149 Fay Throughway Building Number : 1948')#country, city, province, neighbourhood, address
        if i == 25:
            Address.objects.create(user=user,country='United States',city = 'South Hazelfurt',province='Nebraska',neighborhood='Okuneva Expressway',address= '11501 Valentin Points Building Number : 839')#country, city, province, neighbourhood, address


def create_basket_add_product():
    """Creates baskets for each user , then adds some products to their basket."""
    Basket.objects.all().delete()
    products = Product.objects.all()
    users = User.objects.all()
    for user in users:
        Basket.objects.create(user = user)
    baskets = Basket.objects.all()
    for basket in baskets:
        for product in products:
            if product.product_id % 2 == 0:
                product.count -= 1
                product.basket.add(basket)
                product.save()


def set_products_count_ten():
    """Sets all the products' count ten."""
    products = Product.objects.all()
    for product in products:
        product.count = 10
        product.save()


def set_product_images():
    """Removes all the images associated with a product.Then adds new images to products"""
    product_images_remove_all()
    products = Product.objects.all()
    #images_root_path = os.path.join(settings.MEDIA_ROOT, 'images', 'products')
    for product in products:
        if product.name == 'Black T-Shirt':
            filename = 'btt.jpg'
            image_path = os.path.join('images','products',filename)
            product.image.name = image_path
            product.save()
        if product.name == 'Blue T-Shirt':
            filename = 'bluett.jpg'
            image_path = os.path.join('images','products',filename)
            product.image.name = image_path
            product.save()
        if product.name == 'Red T-Shirt':
            filename = 'redtt.jpg'
            image_path = os.path.join('images','products',filename)
            product.image.name = image_path
            product.save()
        if product.name == 'White T-Shirt':
            filename = 'wtt.jpg'
            image_path = os.path.join('images','products',filename)
            product.image.name = image_path
            product.save()


def product_images():
    products = Product.objects.all()
    for product in products:
        print(product.image)

def product_images_remove_all():
    products = Product.objects.all()
    for product in products:
        product.image.delete()
        product.save()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjActStore.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


