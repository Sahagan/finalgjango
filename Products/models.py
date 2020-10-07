from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=128, )
    product_description = models.TextField()
    product_price = models.DecimalField(decimal_places=2, max_digits=7)  
  