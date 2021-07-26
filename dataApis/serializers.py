from django.db.models import fields
from rest_framework import serializers
from dataApis.models import Questionnaire, Job, Todo


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = "__all__"


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
