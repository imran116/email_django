from django.db import models


# Create your models here.

class Subscriber(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)


class SendMail(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()


class Message(models.Model):
    message = models.TextField()


class Order(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField(max_length=150,)
    product_name = models.CharField(max_length=30)
    product_price = models.DecimalField(max_digits=30, decimal_places=2, default=0.00)
    message = models.ForeignKey(Message, on_delete=models.CASCADE,blank=True, null=True)
