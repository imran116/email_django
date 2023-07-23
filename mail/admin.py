from django.contrib import admin

from mail.models import Subscriber, SendMail

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(SendMail)