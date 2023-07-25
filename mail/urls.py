from django.urls.conf import path
from . import views

urlpatterns = [
path('',views.HomeView.as_view(),name='home'),
path('subscripion/',views.SubscriberView.as_view(),name='subscription'),
path('send-mails-all/',views.SendMail.as_view(),name='send-mail'),
path('place-order/',views.place_order,name='place-order')

]