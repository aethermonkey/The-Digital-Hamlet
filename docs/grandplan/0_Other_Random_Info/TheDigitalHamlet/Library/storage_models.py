from django.db import models
from django.db.models import JSONField
import uuid

class Conversation(models.Model):
    
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agents = JSONField()
    users = models.JSONField()

    def __str__(self):
        return f"Conversation {self.conversation_id} between {', '.join(str(agent) for agent in self.agents)}"

class Message(models.Model):
    
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.message_id} in Conversation {self.conversation.conversation_id}"

class Knowledge(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_outdated = models.BooleanField(default=False)



    def __str__(self):
        return self.title


