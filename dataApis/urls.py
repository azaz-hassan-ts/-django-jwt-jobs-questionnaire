from django.conf.urls import url
from django.urls.conf import path, re_path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Data API formats",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.dataapis.com/policies/terms/",
        contact=openapi.Contact(email="azaz.hassan@techno-soft.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = "dataapi"

urlpatterns = [
    url(
        r"^dataapi$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("jobs/", views.Jobs_list.as_view(), name="jobs_list"),
    path("jobs/<int:id>", views.Jobs_details.as_view(), name="jobs_details"),
    path(
        "questionnaire/<int:id>",
        views.Questionnaire_details.as_view(),
        name="questionnaire_details",
    ),
    path(
        "questionnaire/", views.Questionnaire_list.as_view(), name="questionnaire_list"
    ),
    path("todo/", views.Todo_list.as_view(), name="todo_list"),
    path("todo/<int:id>", views.Todo_details.as_view(), name="todo_details"),
]
