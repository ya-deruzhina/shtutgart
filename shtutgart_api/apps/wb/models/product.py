from django.db import models

class ProductModel (models.Model):
    id = models.IntegerField(primary_key=True)
    name_product = models.CharField(max_length=200)
    type_product = models.CharField(max_length=100)
    root_type_product = models.CharField(max_length=50)
    vendor_code = models.CharField(max_length=20)
    description = models.TextField()
    color = models.CharField(max_length=50)
    contents = models.TextField()
    brand_name = models.CharField(max_length=50)
    price_without_nds = models.FloatField()
    price = models.FloatField()
    options = models.TextField()
