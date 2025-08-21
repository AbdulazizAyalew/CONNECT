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
            messages.success(request, "Your account has been created. Please log in.")
            return redirect("login") # we'll add a quick login view in step 7
    else:
        form = CustomUserCreationForm()


    return render(request, "users/base.html", {"form": form})