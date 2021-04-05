from django.db import models


class product(models.Model):
    name = models.CharField(max_length=225)
    price= models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)

class offer(models.Model):
    code= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    discount=models.FloatField()

