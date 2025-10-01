from django.contrib import admin
from django.urls import include, path

from account import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('signin/', views.signup_user, name='signin'),
]
