from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics, serializers, status, viewsets, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import (
    RegistrationSerializer,
    LoginSerializer,
    ProfileSerializer,
    LogoutSerializer,
)
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
def homepage(request):
    return HttpResponse("Hello World")


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)


class LogoutView(generics.CreateAPIView):
    serializer_class = LogoutSerializer

    def post(self, request):
        Refresh_token = request.data["refresh"]
        token = RefreshToken(Refresh_token)
        token.blacklist()
        return Response("Successful Logout", status=status.HTTP_204_NO_CONTENT)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, format=None):
        if request.data == {}:
            return Response(
                {"message": "Send request Body"}, status=status.HTTP_204_NO_CONTENT
            )

        register_serializer = RegistrationSerializer(data=request.data)
        if register_serializer.is_valid():
            register_serializer.save()
            return Response(
                {
                    "data": register_serializer.data,
                    "message": "You are succesfully registered",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.CreateAPIView):
    queryset = User.objects.all()
    http_method_names = ["get", "put"]

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return ProfileSerializer

    def get(self, request, format=None):
        if request.method == "GET":
            username = str(request.user)
            user = User.objects.get(username=username)
            if user.is_active:
                return Response(
                    {
                        "username": user.username,
                        "email": user.email,
                    }
                )
            return Response(
                {"message": "Your account is disabled. Please log in again"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

    def put(self, request, format=None):
        if request.method == "PUT":
            try:
                user = User.objects.get(username=str(request.user))
            except User.DoesNotExist:
                return Response(
                    {"message": "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND
                )

            user_data = JSONParser().parse(request)
            user_serializer = self.get_serializer_class()
            user_serializer = user_serializer(user, user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(
                    {
                        "message": "Data has been updated succesfully",
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "Invalid Information"}, status=status.HTTP_400_BAD_REQUEST
            )


@api_view(["GET"])
@permission_classes((AllowAny,))
def version1(request):
    return Response({"version": request.version}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes((AllowAny,))
def version2(request):
    return Response({"version": request.version}, status=status.HTTP_200_OK)
