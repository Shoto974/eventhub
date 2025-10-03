from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from events.models import Event
from participation.models import Participation


# Create your views here.
@login_required
@require_POST
def remove_participation(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    qs = Participation.objects.filter(event=event, user=request.user)
    if qs.exists():
        qs.delete()
        messages.success(request, "Participation supprimée")
    else:
        messages.info(request, "Tu n'es pas inscrit à cet event")

    return redirect("events_list")