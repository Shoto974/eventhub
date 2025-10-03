from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['note', 'comment']
        widgets = {
            'note': forms.NumberInput(attrs={
                'class': 'w-full border rounded-md p-2 focus:ring-2 focus:ring-blue-500',
                'min': 1,
                'max': 5,
                'placeholder': 'Note sur 5',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'w-full border rounded-md p-2 focus:ring-2 focus:ring-blue-500',
                'rows': 4,
                'placeholder': 'Votre avis...',
            }),
        }