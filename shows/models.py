from django.db import models


COVER_CHOICES = (
    ('0', "$0"),
    ('1-4', "$1-4"),
    ('5-9', "$5-9"),
    ('10-14', "$10-14"),
    ('15-19', "$15-19"),
    ('20+', "$20 or more"),
    ('unknown', "Unknown"),
)

class Venue(models.Model):
    venue_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    venue_website = models.CharField(max_length=50)
    def get_absolute_url(self):
        return "/venues/%i/" % self.id
    def __unicode__(self):
        return self.venue_name

class Genre(models.Model):
    genre = models.CharField(max_length=50)
    def get_absolute_url(self):
        return "/genres/%i/" % self.id
    def __unicode__(self):
        return self.genre

class Band(models.Model):
    band_name = models.CharField(max_length=200)
    band_genres = models.ManyToManyField(Genre)
    band_website = models.CharField(max_length=200)
    def get_absolute_url(self):
        return "/bands/%i/" % self.id
    def __unicode__(self):
        return self.band_name

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField('event date')
    start_time = models.TimeField('event time')
    band_names = models.ManyToManyField(Band)
    cover = models.CharField(max_length=20, choices=COVER_CHOICES)
    event_genres = models.ManyToManyField(Genre)
    venue_name = models.ForeignKey(Venue)
    def get_absolute_url(self):
        return "/events/%i/" % self.id
    def __unicode__(self):
        return self.event_name
