# users/urls.py
from django.urls import path
from . import views

app_name = "laptops"
urlpatterns = [
    path('', views.home, name='home'),
]