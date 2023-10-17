from django.db import models
from ..TheDigitalHamlet import base_models

class BulletinBoard(models.Model):
    entry_id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_by = models.ForeignKey(base_models.BaseAgent.agent_id, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expired_at = models.DateTimeField(null=True)
    clearance

    class meta:
        abstract = True