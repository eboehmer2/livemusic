from django.db import models

GENRE_CHOICES = (
    ('acoustic', "Acoustic"),
    ('alternative', "Alternative"),
    ('bluegrass', "Bluegrass"),
    ('blues', "Blues"),
    ('country', "Country"),
    ('electronic', "Electronic & Techno"),
    ('folk', "Folk"),
    ('funk', "Funk"),
    ('gospel', "Gospel & Religious"),
    ('hip hop', "Hip Hop & Rap"),
    ('indie', "Indie"),
    ('instrumental', "Instrumental"),
    ('jazz', "Jazz"),
    ('latin', "Latin"),
    ('metal', "Metal"),
    ('pop', "Pop"),
    ('punk', "Punk"),
    ('r&b', "R&B"),
    ('reggae', "Reggae"),
    ('rock', "Rock"),
    ('rock-n-roll', "Rock-n-Roll"),
    ('soul', "Soul"),
    ('world', "World"),
    ('other', "Other"),
    ('n_a', "N/A"),
)

COVER_CHOICES = (
    ('0', "$0"),
    ('1-4', "$1-4"),
    ('5-9', "$5-9"),
    ('10+', "$10 or more"),
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

class Band(models.Model):
    band_name = models.CharField(max_length=200)
    genre_1 = models.CharField(max_length=50, choices=GENRE_CHOICES)
    genre_2 = models.CharField(max_length=50, choices=GENRE_CHOICES)
    genre_3 = models.CharField(max_length=50, choices=GENRE_CHOICES)
    band_website = models.CharField(max_length=200)
    def get_absolute_url(self):
        return "/bands/%i/" % self.id
    def __unicode__(self):
        return self.band_name

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField('event date')
    start_time = models.TimeField('event time')
    band_name_1 = models.ForeignKey(Band, related_name='event_band_name_1')
    band_name_2 = models.ForeignKey(Band, related_name='event_band_name_2')
    band_name_3 = models.ForeignKey(Band, related_name='event_band_name_3')
    cover = models.CharField(max_length=20, choices=COVER_CHOICES)
    genre_1 = models.CharField(max_length=50, choices=GENRE_CHOICES)
    genre_2 = models.CharField(max_length=50, choices=GENRE_CHOICES)
    genre_3 = models.CharField(max_length=50, choices=GENRE_CHOICES)
    venue_name = models.ForeignKey(Venue, related_name='event_venue_name')
    def get_absolute_url(self):
        return "/events/%i/" % self.id
    def __unicode__(self):
        return self.event_name
