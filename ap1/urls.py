from django.urls import path
from ap1 import views

urlpatterns = [
    path('',views.index,name='home'),
    path('plants',views.plants,name='plants'),
    path('contact',views.contact,name='contact'),
    path('myaccount',views.myaccount,name='myaccount'),
    path('category/<int:cid>/',views.category,name='category'),


]

