from typing import Optional
from django.db import models

# Create your models here.
class Jobs(models.Model):
    title = models.TextField()
    type = models.CharField(max_length=10)
    score = models.IntegerField()
    weight = models.IntegerField()
    optional = models.BooleanField()

    def __str__(self):
        return f"Title: {self.title}"
