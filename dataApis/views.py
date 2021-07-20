from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework import status
from dataApis.models import Questionnaire, Job
from dataApis.serializers import QuestionnaireSerializer
from rest_framework.response import Response

# Create your views here.


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


@api_view(["GET"])
@permission_classes((AllowAny,))
def jobs_view(request):
    jobs = Job.objects.all()
    my_response = []
    for i in range(len(jobs)):
        my_response.append(convertToJson(jobs[i]))
    return JsonResponse(my_response, safe=False)


@api_view(["GET"])
@permission_classes((AllowAny,))
def questionnaire_details(request, id):
    try:
        questions = Questionnaire.objects.get(id=id)
    except Questionnaire.DoesNotExist:
        return JsonResponse(
            {"message": "The Question does not exist."},
            status=status.HTTP_404_NOT_FOUND,
        )
    questions_serializer = QuestionnaireSerializer(questions)
    return JsonResponse(questions_serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes((AllowAny,))
def questionnaire_list(request):
    questions = Questionnaire.objects.all()
    questions_serializer = QuestionnaireSerializer(questions, many=True)
    return JsonResponse(
        questions_serializer.data, safe=False, status=status.HTTP_200_OK
    )
