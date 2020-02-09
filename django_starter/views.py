from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.price = 700
    dest1.name = 'Tehran'
    dest1.desc = 'A lovely place!'
    dest1.img = 'destination_1.jpg'
    dest1.offer = True

    dest2 = Destination()
    dest2.price = 678
    dest2.name = 'LA'
    dest2.desc = 'A superb place!'
    dest2.img = 'destination_2.jpg'
    dest2.offer = False

    dest3 = Destination()
    dest3.price = 594
    dest3.name = 'Istanbul'
    dest3.desc = 'A dull place!'
    dest3.img = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
