from livemusic.shows.models import Venue, Band, Event
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def homepage(request):
    latest_event_list = Event.objects.all().order_by('event_date')[:5]
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

def banddetail(request, band_id):
    b = get_object_or_404(Band, pk=band_id)
    events = Event.objects.filter(band_names=b)
    return render_to_response('banddetail.html', {'band': b, 'events': events},
                               context_instance=RequestContext(request))

def eventdetail(request, event_id):
    e = get_object_or_404(Event, pk=event_id)
    return render_to_response('eventdetail.html', {'event': e},
                               context_instance=RequestContext(request))

def venuedetail(request, venue_id):
    v = get_object_or_404(Venue, pk=venue_id)
    events = Event.objects.filter(venue_name=v)
    return render_to_response('venuedetail.html', {'venue': v, 'events': events},
                               context_instance=RequestContext(request))

