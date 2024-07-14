from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def _create_user(self, phone,dial_code,country_code, password,**extra_fields):
        user = self.filter(phone = phone).first()
        if user is not None:
            raise Exception("User already exists")
        else:
            user = self.model(phone = phone,dial_code = dial_code,country_code = country_code,**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone,dial_code,country_code,password,**extra_fields):
        return self._create_user(phone,dial_code,country_code,password,**extra_fields)

    def create_superuser(self, phone,dial_code,country_code,password,**extra_fields):
        user = self.create_user(phone,dial_code,country_code,password,**extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class User(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    phone = models.CharField(max_length=15, unique=True,null=False)
    dial_code = models.CharField(max_length=5, null=False,blank=True)
    country_code = models.CharField(max_length=2, null=False,blank=True)
    password = models.CharField(max_length=255, null=False,blank=False)
    name = models.CharField(max_length=255,null=True,blank=True)
    surname = models.CharField(max_length=255,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)

    last_login = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['dial_code','country_code','password']
    USERNAME_FIELD = 'phone'

    objects = UserManager()

    def __str__(self):
        return str({
            'id':self.id,
            'phone':self.phone,
            'dial_code':self.dial_code,
            'country_code':self.country_code,
            'name':self.name,
            'surname':self.surname,
            'age':self.age
        })






