from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from events.forms import EventForm
from events.models import Event, Category


# Create your views here.
def events_list(request):
    events = Event.objects.all()
    categories = Category.objects.all()
    print(categories)
    return render(request, 'events/events.html',
                  {'events':events, 'categories':categories, 'user':request.user})

def events_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('events_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form':form})

def event_update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form':form})

def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('events_list')
    return render(request, 'events/events_list.html', {'event':event})


def events_filtered(request):
    date_deb = request.GET.get('date_deb')
    date_fin = request.GET.get('date_fin')
    category = request.GET.get('category')
    capacity = request.GET.get('capacity')

    qs = Event.objects.all()
    html = ""

    if date_deb:
        qs = qs.filter(date__gte=date_deb)

    if date_fin:
        qs = qs.filter(date__lte=date_fin)

    if category:
        qs = qs.filter(category_id=category)

    if capacity:
        qs = qs.filter(capacity__lte=capacity)

    html = render_to_string('events/event_card.html', {
        'events': qs,
        'user': request.user
    })

    return HttpResponse(html)