from django.db import models
from django.contrib.postgres.fields import JSONField

class Conversation(models.Model):
    agents = JSONField()
    users = models.JSONField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation between {', '.join(str(agent) for agent in self.agents)}"

    