from django import forms
from django.forms import inlineformset_factory

from .models import Event, EventImage


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'category', 'date', 'location', 'capacity']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full border rounded-md p-2 focus:ring-2 focus:ring-blue-500'}),
            'description': forms.Textarea(attrs={'class': 'w-full border rounded-md p-2 focus:ring-2 focus:ring-blue-500', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'w-full border rounded-md p-2 focus:ring-2 focus:ring-blue-500'}),
            'date': forms.DateInput(attrs={'class': 'w-full border rounded-md p-2 focus:ring-2 focus:ring-blue-500', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'w-full border rounded-md p-2 focus:ring-2 focus:ring-blue-500'}),
            'capacity': forms.NumberInput(attrs={'class': 'w-full border rounded-md p-2 focus:ring-2 focus:ring-blue-500'}),
        }



EventImageFormSet = inlineformset_factory(
    Event, EventImage,
    fields=['url'], extra=1,
    widgets={
        'url': forms.URLInput(attrs={'class': 'w-full border rounded-md p-2 focus:ring-2 focus:ring-blue-500'})
    }
)
