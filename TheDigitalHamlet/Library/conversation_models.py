from django.db import models
from django.contrib.postgres.fields import JSONField

class Conversation(models.Model):
    
    conversation_id = models.UUIDField(editable=False)
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agents = JSONField()
    users = models.JSONField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id} between {', '.join(str(agent) for agent in self.agents)}"

    
