from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class ApiUser(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)




class Warhouse(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.PositiveIntegerField()


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    warhouse_id = models.ForeignKey(Warhouse, related_name="products", on_delete=models.CASCADE)