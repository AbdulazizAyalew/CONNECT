from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from .forms import CustomUserCreationForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() # ✅ Creates user in auth_user
            return redirect("registration_success") # we'll add a quick login view in step 7
    else:
        form = CustomUserCreationForm()


    return render(request, "users/register.html", {"form": form})

def registration_success(request):
    return render(request, "users/registration_success.html")

