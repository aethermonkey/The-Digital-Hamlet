from django.db import models

class Conversation(models.Model):
    agent1 = models.ForeignKey('LibraryAgent', on_delete=models.CASCADE)
    agent2 = models.ForeignKey('LibraryAgent', on_delete=models.CASCADE)
    user = models.ForeignKey('SovereignUser', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation between {self.agent1} and {self.agent2}"
