from django.http import HttpResponse
from django.shortcuts import render
from .models import place,programmers


# Create your views here.

def demo(request):
    obj=place.objects.all()
    object=programmers.objects.all()
    return render(request,"index.html",{'result':obj,'val':object})

