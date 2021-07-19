from typing import Optional
from django.db import models
from django.contrib.postgres.fields import ArrayField
from rest_marshmallow import Schema, fields

# Create your models here.
class Questionnaire(models.Model):
    TYPE_CHOICES = [
        ("mcq", "Multiple Choice Question"),
        ("numeric", "Number Based Question"),
        ("text", "Text Based Question"),
        ("code", "Coding Question"),
    ]
    title = models.TextField()
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default="mcq",
    )
    score = models.IntegerField()
    weight = models.IntegerField()
    optional = models.BooleanField()
    options = ArrayField(models.CharField(max_length=10), blank=True, default=list)

    def __str__(self):
        return f"Title: {self.title}"


class Job(models.Model):
    title = models.TextField()
    technologies = ArrayField(models.CharField(max_length=15), blank=True, default=list)
    description = models.TextField()
    salary = ArrayField(models.IntegerField(), size=2)
    type = models.CharField(max_length=15)
    experience = ArrayField(models.IntegerField(), size=2)
    category = models.CharField(max_length=15)
    active = models.BooleanField()
