from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

def show(request):
     return render(request,'myaccount.html')



def login(request):
     if request.method=="POST":
        uname=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=uname,password=pswd)
        if user is not None:
            auth.login(request, user)
            return render(request,'myaccount.html')
        else:
            return render(request,'login.html',{'error': "Invalide Login credentials"})        
     return render(request,'login.html')
def logout(request):
   auth.logout(request)
   return redirect('/')
def registeration(request):
     if request.method=="POST":
        if request.POST['password'] == request.POST['passwordagain']:
           try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'register.html',{'error': "Username has already been taken"})
           except User.DoesNotExist:     
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
                auth.login(request, user)
                return render(request,'myaccount.html')    
        else:
              return render(request,'register.html',{'error': "Passwords Don't Match"})

     else:
          return render(request,'register.html')              
      