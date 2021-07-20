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
from .helperMethods import convertToJson, isTypeValidityCheck
from rest_framework.parsers import JSONParser


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes((AllowAny,))
def jobs_view(request):
    if request.method == "GET":
        jobs = Job.objects.all()
        my_response = []
        for i in range(len(jobs)):
            my_response.append(convertToJson(jobs[i]))
        return JsonResponse(my_response, safe=False)

    elif request.method == "POST":
        try:
            job_data = JSONParser().parse(request)
        except:
            return JsonResponse(
                {"error": "Data format is not correct"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return JsonResponse(job_data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes((AllowAny,))
def questionnaire_details(request, id):
    try:
        questions = Questionnaire.objects.get(id=id)
    except Questionnaire.DoesNotExist:
        return JsonResponse(
            {"message": "The Question does not exist."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        question_serializer = QuestionnaireSerializer(questions)
        return JsonResponse(question_serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        questions.delete()
        return JsonResponse(
            {"message": "Question was succesfully deleted."},
            status=status.HTTP_204_NO_CONTENT,
        )

    elif request.method == "PUT":
        try:
            question_data = JSONParser().parse(request)
            if isTypeValidityCheck(question_data) == 1:
                return JsonResponse(
                    {"message": "MCQ Options can't be empty"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif isTypeValidityCheck(question_data) == 2:
                return JsonResponse(
                    {"message": "Type other than mcq can't have options"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                pass
        except:
            return JsonResponse(
                {"error": "Data couldn't be parsed"}, status=status.HTTP_400_BAD_REQUEST
            )
        question_serializer = QuestionnaireSerializer(questions, data=question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            update = question_serializer.data
            update["message"] = "Successfully Updated"
            return JsonResponse(update, status=status.HTTP_200_OK)
        return JsonResponse(
            question_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET", "POST"])
@permission_classes((AllowAny,))
def questionnaire_list(request):
    if request.method == "GET":
        questions = Questionnaire.objects.all()
        questions_serializer = QuestionnaireSerializer(questions, many=True)
        return JsonResponse(
            questions_serializer.data, safe=False, status=status.HTTP_200_OK
        )
    elif request.method == "POST":
        try:
            question_data = JSONParser().parse(request)
            if isTypeValidityCheck(question_data) == 1:
                return JsonResponse(
                    {"message": "MCQ Options can't be empty"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif isTypeValidityCheck(question_data) == 2:
                return JsonResponse(
                    {"message": "Type other than mcq can't have options"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif isTypeValidityCheck(question_data) == 3:
                return JsonResponse(
                    {"message": "mcq options should be equal to 4"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                pass
        except:
            return JsonResponse(
                {"error": "Data format is not correct"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        question_serializer = QuestionnaireSerializer(data=question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            created = question_serializer.data
            created["message"] = "Successfully Created"
            return Response(
                created,
                status=status.HTTP_201_CREATED,
            )

        return JsonResponse(
            question_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
