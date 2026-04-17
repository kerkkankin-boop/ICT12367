from django.shortcuts import render
from django.http import HttpResponse
from .models import Person 

#

def index(request):
  
    persons = Person.objects.all() 
    
    
    return render(request, "index.html", {'persons': persons})

def about(request):
    return HttpResponse("<h1>เกี่ยวกับเรา</h1>")

def form(request):
    return render(request, 'form.html') 

def contact(request):
    return HttpResponse("<h1>68102067 เกริกกานต์ กิ่งแก้ว</h1>")