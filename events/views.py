from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from events.forms import EventForm, EventImageFormSet
from reviews.models import Review
from events.forms import EventForm
from events.models import Event, Category


@login_required
def events_list(request):
    events = Event.objects.all()

    if request.user.role == "orga":
        events = events.filter(organizer=request.user)
    categories = Category.objects.all()
    print(categories)
    return render(request, 'events/events.html',
                  {'events':events, 'categories':categories, 'user':request.user})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.user.is_staff:
        reviews = Review.objects.filter(event=event).order_by('-created_at')
    else:
        reviews = Review.objects.filter(event=event, validated=True).order_by('-created_at')

    if request.method == 'POST':
        if "add_review" in request.POST:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.event = event
                review.user = request.user
                review.validated = False
                review.save()
                return redirect('event_detail', event_id=event.id)

        if "validate_review" in request.POST and request.user.is_staff:
            review_id = request.POST.get("review_id")
            review = get_object_or_404(Review, pk=review_id)
            review.validated = True
            review.save()
            return redirect('event_detail', event_id=event.id)

    else:
        form = ReviewForm()

    return render(request, "events/event_detail.html", {
        "event": event,
        "reviews": reviews,
        "form": form,
    })

@login_required
def events_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        formset = EventImageFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            formset.instance = event
            formset.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()
        formset = EventImageFormSet()
    return render(request, 'events/event_form.html', {'form':form, 'formset':formset})

@login_required
def event_update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        formset = EventImageFormSet(request.POST, instance=event)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
        formset = EventImageFormSet(instance=event)
    return render(request, 'events/event_form.html', {'form':form, 'formset':formset})

@login_required
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