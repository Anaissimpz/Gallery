from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Category,Location

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def picture_of_day(request):
    
    date = dt.date.today()
    pictures = Image.objects.all()
    return render(request, 'all-pictures/home.html', {"date": date,"pictures":pictures})
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.get_category_images(search_term)
        message = f"{search_term}"

        return render(request, 'all-pictures/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pictures/search.html',{"message":message})
def location (request, location_id):
   location = Location.objects.get(id = location_id)
   images = Image.objects.filter(location = location.id)
   return render(request,'all-pictures/location.html', {"images":images, "location":location})

def share(request,id):
    image=Image.share(id=id)
    return redirect(pic_of_day)
