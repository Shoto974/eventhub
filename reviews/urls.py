from django.urls import path
from . import views

urlpatterns = [
    path('',views.reviews_list,name='events_list'),
]