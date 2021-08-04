from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})




def profile(request):
    return render(request,'profile.html')

def chennai(request):
    chens=ChennaiRestaurant.objects.all()
    return render(request,'chennai.html',{'chens':chens})

def dishes(request):
    return render(request,'dishes.html')