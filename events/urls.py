from django.urls import path
from . import views

urlpatterns = [
    path('',views.events_list,name='events_list'),
    path('add/',views.events_add,name='events_add'),
    path('<int:event_id>/',views.event_update,name='event_update'),
    path('<int:event_id>/delete/',views.event_delete,name='event_delete'),
]