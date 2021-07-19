from django.db.models import fields
from rest_framework import serializers
from dataApis.models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = "__all__"
