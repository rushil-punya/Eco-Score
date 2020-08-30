from django.shortcuts import render
from django.http import HttpResponse
from .models import Cell
import pprint
from django.urls import resolve
from login.models import Profile
from django.contrib.auth.models import User
from .forms import SuggestionsForm
from django.core.mail import send_mail
from django.conf import settings

#this is where the magic happens

#this function is what's initially called when entering the ecoscore app
def charts(request):
    #this allows the form to be filled out and sends an email to me when
    #people submit it
    form = SuggestionsForm(request.POST)
    if form.is_valid():
        senderData = form.cleaned_data['data']
        email_from = settings.EMAIL_HOST_USER
        send_mail( 'ECO SCORE SUGGESTION', senderData, email_from, ['ecoscore9@gmail.com'])
    else:
        form = SuggestionsForm()

    #this parses the database and displays all the cells available along with
    #setting the user's eco score to 0
    cells = Cell.objects.all().filter()
    user = User.objects.get(username=request.user)
    user.profile.ecoNum = 0
    user.save()
    return render(request, 'charts.html', {'cells': cells, 'form': form})

    #this calculates the ecoscore of the user
def calculate(request):
    user = User.objects.get(username=request.user)
    cells = Cell.objects.all().filter(isSelected = True)
    #loops through all cells and checks which ones are selected
    for cell in cells:
        user.profile.ecoNum += cell.numPoints
    user.save()
    Cell.objects.all().update(isSelected = False)
    ecoScore = user.profile.ecoNum
    #calculates average of all users
    numUsers = 0
    average = 0
    allUsers = User.objects.all()
    for oneUser in allUsers:
        numUsers += 1
        average += oneUser.profile.ecoNum
    average = average/numUsers
    return render(request, 'chartsScore.html', {'ecoScore': ecoScore, 'average': int(average)})

#this method redirects to the unique extention of each button and then sets
#it as selected for later calculation
def select(request, slug):
    form = SuggestionsForm(request.POST)
    #allows users to fill out the form which emails the data back to me
    if form.is_valid():
        senderData = form.cleaned_data['data']
        email_from = settings.EMAIL_HOST_USER
        send_mail( 'ECO SCORE SUGGESTION', senderData, email_from, ['ecoscore9@gmail.com'])
    else:
        form = SuggestionsForm()
    select = Cell.objects.filter(slug = slug).update(isSelected = True)
    cells = Cell.objects.all().filter()
    return render(request, 'charts.html', {'cells': cells, 'form': form})

