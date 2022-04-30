from django.shortcuts import render
from ap1.models import Pro,Contact,Plants,Category
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
     datas= Pro.objects.all()
     return render(request,'index.html',{'datas':datas})


def plants(request):
     plants= Plants.objects.all()
     cats=Category.objects.all()
     return render(request,'plants.html',{'plants': plants,'cats':cats})    
def category(request,cid):
    
     cats=Category.objects.all()
     category=Category.objects.get(pk=cid)
     
     plants= Plants.objects.filter(cat=category)
     return render(request,'plants.html',{'plants': plants,'cats':cats})    





def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your massage has bean sent!')     
    return render(request,'contact.html')


def myaccount(request):
     return render(request,'myaccount.html')
