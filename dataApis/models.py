from django.utils import timezone
from typing import Optional
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import DateField

# Create your models here.


class Form(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.title


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
    options = ArrayField(
        models.CharField(max_length=10),
        blank=True,
        default=list,
    )
    # form = models.ForeignKey(Form, related_name="questions")

    def __str__(self):
        return f"Title: {self.title}"


class Job(models.Model):
    title = models.TextField()
    technologies = ArrayField(models.CharField(max_length=50), default=list, blank=True)
    description = models.TextField()
    salary_min = models.IntegerField(default=70000)
    salary_max = models.IntegerField(default=100000)
    type = models.CharField(max_length=50, default="Full Time")
    experience_min = models.IntegerField(default=0)
    experience_max = models.IntegerField(default=1)
    category = models.CharField(max_length=50, default="Development")
    active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Todo(models.Model):
    todo_data = models.TextField()
    is_done = models.BooleanField()

    def __str__(self):
        return self.todo_data
