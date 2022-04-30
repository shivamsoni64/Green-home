from django.urls import path
from ap3 import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.registeration,name='register'),
    path('logout',views.logout,name='logout'),
    
]

