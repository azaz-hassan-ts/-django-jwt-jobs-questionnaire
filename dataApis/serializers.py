from django.db.models import fields
from rest_framework import serializers
from dataApis.models import Questionnaire, Job, Todo, Form
from django.contrib.postgres.fields import ArrayField


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ["title", "type", "score", "weight", "optional", "options"]


class FormSerializer(serializers.ModelSerializer):
    questions = QuestionnaireSerializer(many=True)

    class Meta:
        model = Form
        fields = ["title", "description", "questions"]

    def create(self, validated_data):
        questions_data = validated_data.pop("questions")
        form = Form.objects.create(**validated_data)
        for question_data in questions_data:
            Questionnaire.objects.create(form=form, **question_data)
        return form


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
