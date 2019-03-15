from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def picture_of_day(request):
    
    date = dt.date.today()
    pictures = Image.objects.all()
    return render(request, 'all-pictures/home.html', {"date": date,"pictures":pictures})
