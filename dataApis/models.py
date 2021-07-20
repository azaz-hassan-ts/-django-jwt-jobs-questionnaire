from typing import Optional
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import DateField

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
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    type = models.CharField(max_length=15, default="Full Time")
    experience_min = models.IntegerField()
    experience_max = models.IntegerField()
    category = models.CharField(max_length=15, default="Development")
    active = models.BooleanField(default=True)
    meta_createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    meta_updatedAt = models.DateTimeField(auto_now_add=True, blank=True)
    meta_owner = models.CharField(max_length=20)


def convertToJson(object):
    response = {}
    response["id"] = object.id
    response["title"] = object.title
    response["technologies"] = object.technologies
    response["description"] = object.description
    response["salary"] = {"min": object.salary_min, "max": object.salary_max}
    response["type"] = object.type
    response["experience"] = {
        "min": object.experience_min,
        "max": object.experience_max,
    }
    response["category"] = object.category
    response["active"] = object.active
    response["metadata"] = {
        "createdAt": object.meta_createdAt,
        "updatedAt": object.meta_updatedAt,
        "owner": object.meta_owner,
    }
    return response
