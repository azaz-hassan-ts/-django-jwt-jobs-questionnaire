from django.utils import timezone
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic
from rest_framework.permissions import AllowAny
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework import status, generics
from dataApis.models import Questionnaire, Job, Todo
from dataApis.serializers import QuestionnaireSerializer, JobSerializer, TodoSerializer
from rest_framework.response import Response
from .helperMethods import convertToJson, isTypeValidityCheck
from rest_framework.parsers import JSONParser


# Create your views here.


class Jobs_list(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return JobSerializer

    def get(self, request, format=None):
        jobs = Job.objects.all()
        my_response = []
        for i in range(len(jobs)):
            my_response.append(convertToJson(jobs[i]))
        return JsonResponse(my_response, safe=False)

    def post(self, request, format=None):
        try:
            job_data = JSONParser().parse(request)
        except:
            return JsonResponse(
                {"error": "Data format is not correct"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        job_serializer = self.get_serializer_class()
        job_serializer = job_serializer(data=job_data)
        if job_serializer.is_valid():
            job_serializer.save()
            job = convertToJson(Job.objects.last())
            return Response(
                job,
                status=status.HTTP_201_CREATED,
            )

        return JsonResponse(
            job_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class Jobs_details(generics.CreateAPIView):
    http_method_names = ["get", "put", "delete"]
    permission_classes = [AllowAny]
    serializer_class = JobSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return JobSerializer

    def get_job(self, id):
        try:
            job = Job.objects.get(id=id)
        except Job.DoesNotExist:
            return 1
        return job

    def get(self, request, id):
        job = self.get_job(id)
        if job == 1:
            return JsonResponse(
                {"message": "This Job does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return JsonResponse(convertToJson(job), status=status.HTTP_200_OK)

    def delete(self, request, id):
        job = self.get_job(id)
        if job == 1:
            return JsonResponse(
                {"message": "This Job does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        job.delete()
        return JsonResponse(
            {"message": "Job was succesfully deleted."},
            status=status.HTTP_204_NO_CONTENT,
        )

    def put(self, request, id):
        try:
            job_data = JSONParser().parse(request)
        except:
            return JsonResponse(
                {"error": "Data couldn't be parsed"}, status=status.HTTP_400_BAD_REQUEST
            )
        job = self.get_job(id)
        if job == 1:
            return JsonResponse(
                {"message": "This Job does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        job_serializer = JobSerializer(job, data=job_data)
        if job_serializer.is_valid():
            job_serializer.save()
            update = convertToJson(Job.objects.get(id=id))
            update["message"] = "Successfully Updated"
            return JsonResponse(update, status=status.HTTP_200_OK)
        return JsonResponse(
            job_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class Questionnaire_details(generics.CreateAPIView):
    http_method_names = ["get", "put", "delete"]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return QuestionnaireSerializer

    def get_question(self, id):
        try:
            question = Questionnaire.objects.get(id=id)
        except Questionnaire.DoesNotExist:
            return 1
        return question

    def get(self, request, id):
        question = self.get_question(id)
        if question == 1:
            return JsonResponse(
                {"message": "The Question does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        question_serializer = QuestionnaireSerializer(question)
        return JsonResponse(question_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        question = self.get_question(id)
        if question == 1:
            return JsonResponse(
                {"message": "The Question does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        question.delete()
        return JsonResponse(
            {"message": "Question was succesfully deleted."},
            status=status.HTTP_204_NO_CONTENT,
        )

    def put(self, request, id):
        try:
            question_data = JSONParser().parse(request)
            if isTypeValidityCheck(question_data) == 1:
                return JsonResponse(
                    {"message": "MCQ Options can't be empty"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif isTypeValidityCheck(question_data) == 2:
                return JsonResponse(
                    {"message": "MCQ Options can't be less than 2."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif isTypeValidityCheck(question_data) == 3:
                return JsonResponse(
                    {"message": "Type other than mcq can't have options"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif isTypeValidityCheck(question_data) == 4:
                return JsonResponse(
                    {"message": "MCQ Options can't be more than 4."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                pass
        except:
            return JsonResponse(
                {"error": "Data couldn't be parsed"}, status=status.HTTP_400_BAD_REQUEST
            )
        question = self.get_question(id)
        if question == 1:
            return JsonResponse(
                {"message": "The Question does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        question_serializer = QuestionnaireSerializer(question, data=question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            update = question_serializer.data
            update["message"] = "Successfully Updated"
            return JsonResponse(update, status=status.HTTP_200_OK)
        return JsonResponse(
            question_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class Questionnaire_list(generics.CreateAPIView):
    http_method_names = ["get", "post"]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return QuestionnaireSerializer

    def get(self, request):
        questions = Questionnaire.objects.all()
        questions_serializer = QuestionnaireSerializer(questions, many=True)
        return JsonResponse(
            questions_serializer.data, safe=False, status=status.HTTP_200_OK
        )

    def post(self, request):
        try:
            question_data = JSONParser().parse(request)
            if isTypeValidityCheck(question_data) == 1:
                return JsonResponse(
                    {"message": "MCQ Options can't be empty"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif isTypeValidityCheck(question_data) == 2:
                return JsonResponse(
                    {"message": "MCQ Options can't be less than 2."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif isTypeValidityCheck(question_data) == 3:
                return JsonResponse(
                    {"message": "Type other than mcq can't have options"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif isTypeValidityCheck(question_data) == 4:
                return JsonResponse(
                    {"message": "MCQ Options can't be more than 4."},
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


class Todo_list(generics.CreateAPIView):
    http_method_names = ["get", "post"]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TodoSerializer

    def get(self, request):
        todos = Todo.objects.all()
        todos_serializer = TodoSerializer(todos, many=True)
        return JsonResponse(
            todos_serializer.data, safe=False, status=status.HTTP_200_OK
        )

    def post(self, request):
        try:
            todo_data = JSONParser().parse(request)
        except:
            return JsonResponse(
                {"error": "Data format is not correct"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        Todo.objects.all().delete()
        invalid = []
        for i in range(len(todo_data)):
            todo_serializer = TodoSerializer(data=todo_data[i])
            if todo_serializer.is_valid():
                todo_serializer.save()
                created = todo_serializer.data
                created["message"] = "Successfully Created"
            else:
                invalid.append(todo_data[i])

        if invalid == []:
            return JsonResponse(
                {
                    "message": "All Data is added succesfully",
                },
                status=status.HTTP_200_OK,
            )
        return JsonResponse(
            {"message": "Valid Data is added succesfully", "invalid_data": invalid},
            status=status.HTTP_202_ACCEPTED,
        )


class Todo_details(generics.CreateAPIView):
    http_method_names = ["get", "put", "delete"]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return TodoSerializer

    def get_todo(self, id):
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return 1
        return todo

    def get(self, request, id):
        todo = self.get_todo(id)
        if todo == 1:
            return JsonResponse(
                {"message": "The task does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        todo_serializer = TodoSerializer(todo)
        return JsonResponse(todo_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        todo = self.get_todo(id)
        if todo == 1:
            return JsonResponse(
                {"message": "The task does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        todo.delete()
        return JsonResponse(
            {"message": "Task was succesfully deleted."},
            status=status.HTTP_204_NO_CONTENT,
        )

    def put(self, request, id):
        try:
            todo_data = JSONParser().parse(request)
        except:
            return JsonResponse(
                {"error": "Data couldn't be parsed"}, status=status.HTTP_400_BAD_REQUEST
            )
        todo = self.get_todo(id)
        if todo == 1:
            return JsonResponse(
                {"message": "The task does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        todo_serializer = TodoSerializer(todo, data=todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            update = todo_serializer.data
            update["message"] = "Successfully Updated"
            return JsonResponse(update, status=status.HTTP_200_OK)
        return JsonResponse(
            todo_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
