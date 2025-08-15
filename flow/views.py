from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .settings import BASE_DIR
import os

def home_dashboard(request):
    
    return render(request, 'home_dashboard.html')