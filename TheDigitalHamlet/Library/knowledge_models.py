from django.db import models

class Knowledge(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_outdated = models.BooleanField(default=False)



    def __str__(self):
        return self.title


