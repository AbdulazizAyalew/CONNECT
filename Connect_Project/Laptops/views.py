from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Laptop
# Create your views here.

def home(request):
    query = request.GET.get("q", "")  # get search term if any
    
    # filter laptops only if query is given
    if query:
        laptop_list = Laptop.objects.filter(
            Q(name__icontains=query) |
            Q(core__icontains=query) |
            Q(generation__icontains=query)
        )
    else:
        laptop_list = Laptop.objects.all()

    paginator = Paginator(laptop_list, 12) 
    page_number = request.GET.get("page")
    laptops = paginator.get_page(page_number)

    return render(request, "laptops/home.html", {
        'laptops': laptops,
        'query': query
    })
