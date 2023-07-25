from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView

from Email_django import settings
from mail import forms
from mail.models import Subscriber, Message, Order

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


# Order


def place_order(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        customer_email = request.POST['customer_email']
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']

        order = Order.objects.create(
            customer_name=customer_name,
            customer_email=customer_email,
            product_name=product_name,
            product_price=product_price,
        )
        order_confirmation(order)
        messages.success(request, "order confirm!!")

    return render(request, 'place_order.html', )


def order_confirmation(order):
    # Email subject
    subject = 'Your Order Confirmation'
    # Email content (using the HTML template and order data)
    email_content = render_to_string('email_messages.html', {
        'customer_name': order.customer_name,
        'order_id': order.id,
        'product_name': order.product_name,
        'product_price': order.product_price,
    })

    # Sender email (can be your Gmail account or any other email address)
    from_email = settings.EMAIL_HOST_USER

    # Recipient email (the customer's email address)
    to_email = order.customer_email

    # Send the email
    send_mail(subject, '', from_email, [to_email], html_message=email_content)
