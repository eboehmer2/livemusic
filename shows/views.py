from livemusic.shows.models import Venue, Band, Event
from django.shortcuts import render_to_response

def homepage(request):
    events = Event.objects.order_by('event_date')
    return render_to_response('homepage.html', {
        'events': events,
    })
