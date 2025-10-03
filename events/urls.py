from django.urls import path
from . import views

urlpatterns = [
    path('',views.events_list,name='events_list'),
    path('add/',views.events_add,name='event_form'),
    path('<int:event_id>/',views.event_update,name='event_update'),
    path('<int:event_id>/delete/',views.event_delete,name='event_delete'),
    path('<int:event_id>/detail/', views.event_detail, name='event_detail'),
    path("filtered", views.events_filtered,name='events_filtered'),
]