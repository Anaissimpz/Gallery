from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def picture_of_day(request):
    
    date = dt.date.today()
    pics = Image.objects.all()
    return render(request, 'pictures/home.html', {"date": date,"pics":pics})