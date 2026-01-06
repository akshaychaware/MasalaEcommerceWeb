from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Masala(models.Model):
#     name=models.CharField(max_length=300)
#     img=models.ImageField(upload_to='images/')
#     prize=models.FloatField()
#     mrp=models.FloatField()
#     discount=models.IntegerField()
class Masala(models.Model):
    name=models.CharField(max_length=100,null=True)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=20, blank=True, null=True)
    prize=models.FloatField(null=True)
    mrp=models.FloatField(null=True)
    discount=models.IntegerField(null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    ingredients = models.TextField()
    recipe = models.TextField()
    img = models.ImageField(upload_to='assets/images/masala/add_product', blank=True, null=True) # pyright: ignore[reportInvalidStringEscapeSequence]

    def __str__(self):
        return self.name
    

class cart(models.Model):
    uid=models.ForeignKey(User,on_delete= models.CASCADE,db_column="uid")
    pid = models.ForeignKey(Masala, on_delete=models.CASCADE, db_column="pid", default=1)
    qty=models.IntegerField(default=1)

class order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Masala,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

# models.py


