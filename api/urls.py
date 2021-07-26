from django.conf.urls import url
from django.urls.conf import path, re_path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="JWT Auth API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.jwtauth.com/policies/terms/",
        contact=openapi.Contact(email="azaz.hassan@techno-soft.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = "api"

urlpatterns = [
    url(
        r"^$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    # path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    re_path("v1/version", views.version1, name="version1"),
    re_path("v2/version", views.version2, name="version2"),
]
