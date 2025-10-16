
import os
from django.http import HttpResponse
from django.shortcuts import render
from app import settings
os.listdir(settings.BASE_DIR / 'data')

def index(request):
    context = {"name" : "Laetitia", "breadcrumb" : [('Home', '/')]}
    return render(request, "index.html", context)
