from django.db import models
from django.db.models import JSONField
import uuid
from Library.storage_models import Conversation


# Create your models here.
class Rooms(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(Conversation)
    host = models.ForeignKey(Conversation, on_delete=models.CASCADE)
