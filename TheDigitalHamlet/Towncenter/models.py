from django.db import models
from TheDigitalHamlet.TheDigitalHamlet.base_models import GeoEntity

class Towncenter(GeoEntity):
    population = models.PositiveIntegerField()
    area = models.FloatField()
    established_date = models.DateField()
    description = models.TextField()
