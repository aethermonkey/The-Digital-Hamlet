from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from autogen.agentchat.agent import Agent as AutogenAgent


class GeoEntity(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True

class BaseAgent(AutogenAgent, models.Model):
    age = models.PositiveIntegerField()
    location = models.ForeignKey(GeoEntity, on_delete=models.CASCADE)
    traits = models.JSONField(default=dict)
    clearance = models.JSONField(default=dict)
    bank_balance = models.FloatField(default=0.0,)

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
    currency_code = models.CharField(max_length=8)
    location = models.ForeignKey(GeoEntity, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    # The BaseCurrency represents currencies within the digital hamlet.
    # We will likely need to work out some exchange system in future for realizing exchange rates
    # between hamlet currency and outside world currency, like USD, AUD, cryptos, etc.
