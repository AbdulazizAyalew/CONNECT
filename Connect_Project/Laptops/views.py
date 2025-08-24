from django.shortcuts import render,get_object_or_404
from .models import Laptop
# Create your views here.

def home(request):
    return render(request,"laptops/home.html")
