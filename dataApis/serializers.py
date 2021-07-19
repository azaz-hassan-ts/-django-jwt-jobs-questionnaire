from django.db.models import fields
from rest_framework import serializers
from dataApis.models import Jobs


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"
