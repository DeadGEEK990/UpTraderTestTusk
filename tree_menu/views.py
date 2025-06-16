from django.shortcuts import render
from .models import MenuItem


def home_page(request):
    return render(request, "base.html")
