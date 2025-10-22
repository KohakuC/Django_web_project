
import os
import eyed3
from . import models
from django.http import HttpResponse
from django.shortcuts import render
from . import settings

def index(request):
    data_dir = settings.BASE_DIR / 'data'
    tracks = []

    
    musics = [] 
    for rows in models.MyMusic.objects.all():
        musics.append(rows)


    context = {
        "name": "Laetitia",
        "breadcrumb": [('Home', '/')],
        "musics": musics,
    }
    return render(request, "index.html", context)