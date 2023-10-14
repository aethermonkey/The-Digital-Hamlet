from django.db import models
from django.core.validators import MinValueValidator as Min, MaxValueValidator as Max
from django.db.models import CheckConstraint, Q


# Create your models here.
class Trait(models.Model):
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200)
    value = models.FloatField(validators=[Min(-1.0), Max(1.0)])
    description = models.TextField()

    class Meta:
        unique_together = ('agent', 'name')
        constraints = (
            # for checking range in the DB
            CheckConstraint(
                check=Q(value__gte=-1.0) & Q(value__lte=1.0),
                name='value_range'),
            )
