# myapp/forms.py
from django.forms import ModelForm
from django import forms
from .models import artist, duration, title, albums, date_added

class artistForm(ModelForm):
    class Meta:
        model = artist
        fields = "__all__"

class durationForm(ModelForm):
    class Meta:
        model = duration
        fields = "__all__"

class titleForm(ModelForm):
    class Meta:
        model = title
        fields = "__all__"

class albumsForm(ModelForm):
    class Meta:
        model = albums
        fields = "__all__"

class date_addedForm(ModelForm):
    date_added = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = date_added
        fields = "__all__"


