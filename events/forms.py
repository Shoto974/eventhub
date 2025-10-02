from django import forms
from django.forms import inlineformset_factory

from .models import Event, EventImage


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','description','category','date','location','capacity']


EventImageFormSet = inlineformset_factory(
    Event, EventImage,
    fields=['url'], extra=1
)