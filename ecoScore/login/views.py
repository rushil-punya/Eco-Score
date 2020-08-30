from django.shortcuts import render, redirect
from .forms import RegistrationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('../user/', user)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/loginPage.html', {"form": form})
    

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registerPage.html', {"form": form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')
