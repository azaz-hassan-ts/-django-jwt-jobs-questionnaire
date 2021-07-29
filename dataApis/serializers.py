from django.db.models import fields
from rest_framework import serializers
from dataApis.models import Questionnaire, Job, Todo, Form
from django.contrib.postgres.fields import ArrayField


class QuestionnaireSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Questionnaire
        fields = ["id", "title", "type", "score", "weight", "optional", "options"]


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

    def update(self, form, validated_data):
        form.title = validated_data.get("title", form.title)
        form.description = validated_data.get("description", form.description)
        form.save()
        form_questions_dict = dict((i.id, i) for i in form.questions.all())
        questions = validated_data.pop("questions")
        for question in questions:
            if "id" in question:
                form_question = form_questions_dict.pop(question["id"])
                form_question.title = question.get("title", form_question.title)
                form_question.type = question.get("type", form_question.type)
                form_question.score = question.get("score", form_question.score)
                form_question.weight = question.get("weight", form_question.weight)
                form_question.optional = question.get(
                    "optional", form_question.optional
                )
                form_question.options = question.get("options", form_question.options)
                form_question.save()
            else:
                Questionnaire.objects.create(form=form, **question)
        if len(form_questions_dict) > 0:
            for question in form_questions_dict.values():
                question.delete()

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
