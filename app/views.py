
import os
import eyed3
from . import models
from django.http import HttpResponse
from django.shortcuts import render
from . import settings
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from . import forms
from django.utils import timezone
from django.views.generic.list import ListView


class MusicsList(ListView):
    template_name = 'index.html'
    #model = models.MyMusic
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = [('Home', '/')]

        return context
    
    def get_queryset(self):
        return models.MyMusic.objects.all()

class CreateMusic(CreateView):
    model = models.MyMusic
    form_class = forms.MusicForm
    template_name = "add.html"


class DeleteMusic(DeleteView):
    model = models.MyMusic
    template_name = "musics_confirm_delete.html" 
    context_object_name = "music"
    success_url = reverse_lazy("musics_list")

class UpdateMusic(UpdateView):
    model = models.MyMusic
    #fields = ['music_name', 'artist']
    form_class = forms.MusicForm
    template_name = "edit_form.html"   

    def get_success_url(self):
        return reverse_lazy("musics_details", args=[self.object.pk])