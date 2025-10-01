from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.messages import get_messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import logging
from account.forms import CustomUserCreationForm

logger = logging.getLogger(__name__)
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/events')
        else:
            messages.error(request, 'Login ou mot de passe incorrect')
            return redirect('/account/login')
    else:
        return render(request, 'auth/login.html', {})


def signup_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Inscription terminée. Vous pouvez vous connecter.")
            return redirect("login")
        else:
            messages.error(request, 'Erreur lors de l\'inscription')
            return render(request, "auth/signin.html", {"form": form})

    else:
        form = CustomUserCreationForm()
        return render(request, "auth/signin.html", {"form": form})
