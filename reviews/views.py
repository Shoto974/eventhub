from django.shortcuts import render

from events.forms import EventForm
from reviews.models import Review


# Create your views here.

def reviews_list(request):
    reviews = Review.objects.all()
    return render(request,'reviews/reviews_list.html',{'reviews':reviews})

def review_add(request):
    form = EventForm(request.POST)
