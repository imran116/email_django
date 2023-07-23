from django.forms import ModelForm

from mail.models import Subscriber, SendMail


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'


class SendMailForm(ModelForm):
    class Meta:
        model = SendMail
        fields = '__all__'
