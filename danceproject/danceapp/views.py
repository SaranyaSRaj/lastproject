from django.shortcuts import render
from django.http import HttpResponse
from.models import Place
# Create your views here.
from.models import Photos



def demo(request):
    obj = Place.objects.all()
    dvp = Photos.objects.all()
    return render(request,"index.html",{'result':obj,'submit':dvp})




