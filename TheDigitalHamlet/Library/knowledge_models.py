from django.db import models

class Knowledge(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    medium = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
