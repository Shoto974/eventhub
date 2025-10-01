from django.shortcuts import render, redirect, get_object_or_404

from events.forms import EventForm
from events.models import Event


# Create your views here.
def events_list(request):
    events = Event.objects.all()
    return render(request, 'events/events.html', {'events':events})

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