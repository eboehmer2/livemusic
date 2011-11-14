from shows.models import Venue
from shows.models import Event
from shows.models import Band
from shows.models import Genre
from django.contrib import admin

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Band)
admin.site.register(Genre)
