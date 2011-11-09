from livemusic.shows.models import Venue, Band, Event
from django.shortcuts import render_to_response

def homepage(request):
    latest_event_list = Event.objects.all().order_by('event_date')
    return render_to_response('homepage.html', {'latest_event_list': latest_event_list})

def events(request):
    latest_event_list = Event.objects.all().order_by('event_date')
    return render_to_response('events.html', {'latest_event_list': latest_event_list})

def bands(request):
    band_list = Band.objects.all().order_by('band_name')
    return render_to_response('bands.html', {'band_list': band_list})

def venues(request):
    venue_list = Venue.objects.all().order_by('venue_name')
    return render_to_response('venues.html', {'venue_list': venue_list})
