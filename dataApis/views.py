from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import (
    api_view,
    permission_classes,
)

# Create your views here.


@api_view(["GET"])
@permission_classes((AllowAny,))
def jobs_view(request):
    pass


@api_view(["GET"])
@permission_classes((AllowAny,))
def questionnaire_view(request, id):
    pass
