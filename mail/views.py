from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from mail import forms
from mail.models import Subscriber

from django.core.mail import send_mail


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'


class SubscriberView(View):
    def post(self, request):
        form = forms.SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            send_subscription_email(name, email)
            messages.success(request, 'Subscription Successful!')
        else:
            messages.error(request, 'Subscription Failed!')

        return render(request, 'subscriber.html')

    def get(self, request):
        return render(request, 'subscriber.html')


def send_subscription_email(name, email):
    subject = 'Subscription Confirmation'
    message = f'Thank you for subscribing, {name}!'
    from_email = 'hexashophelpcenter@gmail.com'
    recipient = [email]

    email = EmailMessage(subject, message, from_email, recipient)
    email.send()


class SendMail(View):
    def post(self, request):
        email = list(Subscriber.objects.values_list('email', flat=True))
        form = forms.SendMailForm(data=request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mails(subject, message, email)
            messages.success(request, 'Mail Send Successful.')
        else:
            messages.error(request, 'mail failed')

        return render(request, 'email.html')

    def get(self, request):
        return render(request, 'email.html')


def send_mails(subject, message, email):
    from_email = 'hexashophelpcenter@gmail.com'
    recipient = email
    message = message
    subject = subject
    send_mail(subject, message, from_email, recipient, fail_silently=False)
