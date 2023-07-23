from django.db import models


# Create your models here.

class Subscriber(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200,unique=True)

class SendMail(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
