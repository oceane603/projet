from django.urls import path
from shop.views import index, detail,checkout,confirmation,contact,inscription


urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail , name="detail"),
    path('checkout', checkout , name="checkout"),
    path('confirmation', confirmation , name= "confirmation"),
    path('contact', contact , name= "contact"),
    path('inscription', inscription , name= "inscription"),


]
