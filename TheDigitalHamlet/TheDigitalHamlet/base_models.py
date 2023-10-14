from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class GeoEntity(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True

class BaseAgent(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    location = models.ForeignKey(GeoEntity, on_delete=models.CASCADE)
    traits = models.JSONField()

    class Meta:
        abstract = True

class BaseBuilding(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(GeoEntity, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    type = models.CharField(max_length=200)

    class Meta:
        abstract = True

class BaseService(models.Model):
    name = models.CharField(max_length=200)
    provider = models.ForeignKey(BaseAgent, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)

    class Meta:
        abstract = True

class BaseEvent(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(GeoEntity, on_delete=models.CASCADE)
    time = models.DateTimeField()
    participants = models.ManyToManyField(BaseAgent)

    class Meta:
        abstract = True

class BaseItem(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(BaseAgent, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)

    class Meta:
        abstract = True

class BaseCurrency(models.Model):
    name = models.CharField(max_length=200)
    value = models.FloatField()
    currency_code = models.CharField(max_length=8)
    # TODO: Add exchange rate currency codes in order to calculate value again local currency.
    rates = models.JSONField()
    

    class Meta:
        abstract = True
