from django.db import models

VENUENAME_CHOICES = (
    ('zoo', "ZOO Bar"),
    ('duffys', "Duffy's Tavern"),
    ('bourbon', "Bourbon Theatre"),
    ('other', "Other"),
)

ADDRESS_CHOICES = (
    ('136 N. 14th St.', "ZOO Bar"),
    ('1412 O St.', "Duffy's Tavern"),
    ('1415 O St.', "Bourbon Theatre"),
    ('other', "Other"),
)

CITY_CHOICES = (
    ('lincoln', "Lincoln"),
    ('omaha', "Omaha"),
    ('other', "Other"),
)

STATE_CHOICES = (
    ('NE', "Nebraska"),
    ('other', "Other"),
)

ZIP_CHOICES = (
    ('68508', "ZOO Bar"),
    ('68508', "Duffy's Tavern"),
    ('68508', "Bourbon Theatre"),
    ('other', "Other"),
)

PHONE_CHOICES = (
    ('402-435-8754', "ZOO Bar"),
    ('402-474-3543', "Duffy's Tavern"),
    ('402-477-4776', "Bourbon Theatre"),
    ('other', "Other"),
)

EMAIL_CHOICES = (
    ('info@zoobar.com', "ZOO Bar"),
    ('management@duffyslincoln.com', "Duffy's Tavern"),
    ('n/a', "Bourbon Theatre"),
    ('other', "Other"),
)

WEBSITE_CHOICES = (
    ('zoobar.com', "ZOO Bar"),
    ('duffyslincoln.com', "Duffy's Tavern"),
    ('bourbontheatre.com', "Bourbon Theatre"),
    ('other', "Other"),
)

GENRE_CHOICES = (
    ('alt', "Alternative"),
    ('blues', "Blues"),
    ('country', "Country"),
    ('electronic', "Electronic & Techno"),
    ('folk', "Folk"),
    ('gospel', "Gospel & Religious"),
    ('hip hop', "Hip Hop & Rap"),
    ('jazz', "Jazz"),
    ('latin', "Latin"),
    ('metal', "Metal"),
    ('pop', "Pop"),
    ('r&b', "R&B"),
    ('reggae', "Reggae"),
    ('rock', "Rock"),
    ('world', "World"),
    ('other', "Other"),
)

COVER_CHOICES = (
    ('0', "$0"),
    ('1-4', "$1-4"),
    ('5-9', "$5-9"),
    ('10+', "$10 or more"),
)

class Venue(models.Model):
    venue_name = models.CharField(max_length=50, choices=VENUENAME_CHOICES)
    street_address = models.CharField(max_length=50, choices=ADDRESS_CHOICES)
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    state = models.CharField(max_length=5, choices=STATE_CHOICES)
    zip_code = models.CharField(max_length=5, choices=ZIP_CHOICES)
    phone = models.CharField(max_length=12, choices=PHONE_CHOICES)
    email = models.CharField(max_length=50, choices=EMAIL_CHOICES)
    venue_website = models.CharField(max_length=50, choices=WEBSITE_CHOICES)
    def __unicode__(self):
        return self.venue_name

class Band(models.Model):
    band_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    band_website = models.CharField(max_length=200)
    def __unicode__(self):
        return self.band_name

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField('event date')
    start_time = models.TimeField('event time')
    band_name = models.ForeignKey(Band, related_name='event_band_name')
    cover = models.CharField(max_length=20, choices=COVER_CHOICES)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    venue_name = models.ForeignKey(Venue, related_name='event_venue_name')
    def __unicode__(self):
        return self.event_name
