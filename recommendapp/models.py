from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    prod_id = models.CharField(primary_key=True, max_length=500)
    link = models.URLField(max_length=500)
    gender = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    brand = models.CharField(max_length=500)
    price = models.IntegerField()


class Similarity(models.Model):
    target_prod = models.CharField(max_length=500)
    sim_prod = models.CharField(max_length=500)
    similarity = models.FloatField()

    @property
    def target_product(self):
        return Product.objects.get(prod_id=self.target_prod)
    @property
    def sim_product(self):
        return Product.objects.get(prod_id=self.sim_prod)