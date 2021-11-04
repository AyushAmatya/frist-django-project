from django.db import models

# Create your models here.
class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=500)

class Items(models.Model):
    ItemId = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=500)
    ItemInStock = models.IntegerField
