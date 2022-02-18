import datetime
from operator import truediv

from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request): 
    date=datetime.datetime.now() 
    my_dict={'insert_date':date} 
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.img = 'products/products-1.jpg'
    dest1.price = 500
    dest1.desc = "the city that never sleeps"
    dest1.offer = False
    dest2 = Destination()
    dest2.name = "Delhi"
    dest2.img = 'products/products-2.jpg'
    dest2.price = 600
    dest2.desc = "the city that never wake up"
    dest2.offer = True
    dest3 = Destination()
    dest3.name = "GOA"
    dest3.img = 'products/products-3.jpg'
    dest3.price = 700
    dest3.desc = "the city that always party"
    dest3.offer = False
    dests = [dest1, dest2, dest3]
    return render(request,'testApp/index.html', context={'dests': dests}) 