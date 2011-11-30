from shows.models import Venue
from shows.models import Event
from shows.models import Band
from shows.models import Genre
from django.contrib import admin

class BandAdmin(admin.ModelAdmin):
    list_display = ('band_name', 'band_website')
    search_fields = ['band_name']
    filter_horizontal = ['band_genres']

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'start_time', 'venue_name')
    list_filter = ['venue_name', 'event_date', 'start_time']
    date_hierarchy = 'event_date'
    filter_horizontal = ['band_names', 'event_genres']

class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_name', 'city', 'state')
    search_fields = ['venue_name']

class GenreAdmin(admin.ModelAdmin):
    search_fields = ['genre']
    list_display = ('genre', '__unicode__')

admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Genre, GenreAdmin)
