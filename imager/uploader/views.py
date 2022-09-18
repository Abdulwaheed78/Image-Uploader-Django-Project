from django.shortcuts import render,redirect
from uploader import models
from .models import Imager
from email.mime import image

# Create your views here.
def index(request):
    if request.method=="POST":
        im=Imager()
        im.title=request.POST.get('title')
        if len(request.FILES)!=0:
            im.image=request.FILES['image']
        im.save()
        return redirect('/')
    else:
        data=Imager.objects.all()
    return render(request,'index.html',{'data':data})