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
