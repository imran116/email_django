from django.contrib import admin

from mail.models import Subscriber, SendMail, Message

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(SendMail)
admin.site.register(Message)