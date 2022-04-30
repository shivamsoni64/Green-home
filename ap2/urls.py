from django.urls import path
from ap2 import views

urlpatterns = [
    path('cart',views.cart,name='cart')
    
]

