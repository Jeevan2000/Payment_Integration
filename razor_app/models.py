from django.db import models

# Create your models here.


class Donation(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    amount=models.IntegerField()
    paymentid=models.CharField(max_length=300,default="",primary_key=True)
    paid=models.BooleanField(default=False)