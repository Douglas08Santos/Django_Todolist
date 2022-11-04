from django.db import models
from datetime import  datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
