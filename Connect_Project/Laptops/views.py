from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Laptop
# Create your views here.

def home(request):
    laptop_list = Laptop.objects.all()
    paginator = Paginator(laptop_list, 12) 

    page_number = request.GET.get("page")
    laptops = paginator.get_page(page_number)

    return render(request,"laptops/home.html", {'laptops': laptops})
