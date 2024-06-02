from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1  = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = True

    dest2  = Destination()
    dest2.name = 'New York'
    dest2.desc = 'The great City of the World'
    dest2.img = 'destination_2.jpg'
    dest2.price = 705
    dest1.offer = False
    
    dest3  = Destination()
    dest3.name = 'Havana'
    dest3.desc = 'The City ost beautifull'
    dest3.img = 'destination_3.jpg'
    dest3.price = 708
    dest1.offer = True
    
    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})