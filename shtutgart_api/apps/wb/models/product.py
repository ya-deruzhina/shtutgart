from django.db import models

class ProductModel (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    count = models.IntegerField(null=False)