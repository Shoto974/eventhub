from django.urls import path
from . import views

app_name = "participation"

urlpatterns = [
    path("<int:event_id>/unparticipate/", views.remove_participation, name="events_unparticipate"),

]