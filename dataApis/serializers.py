from django.db.models import fields
from rest_framework import serializers
from dataApis.models import Questionnaire, Job, Todo, Form
from django.contrib.postgres.fields import ArrayField


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = "__all__"


class FormSerializer(serializers.ModelSerializer):
    questionnaire = QuestionnaireSerializer(many=True)

    class Meta:
        model = Form
        fields = ["title", "description", "questionnaire"]


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            "title",
            "technologies",
            "description",
            "salary_min",
            "salary_max",
            "type",
            "experience_min",
            "experience_max",
            "category",
            "active",
            "owner",
        )


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
