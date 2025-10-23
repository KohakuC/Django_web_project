from django.forms import ModelForm
from app.models import MyMusic

# Create the form class.
class MusicForm(ModelForm):
    class Meta:
       model = MyMusic
       fields = ["music_name", "artist"]