from django.db import models

class Conversation(models.Model):
    agents = models.ManyToManyField('LibraryAgent')
    users = models.ManyToManyField('SovereignUser')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation between {', '.join(str(agent) for agent in self.agents.all())}"
