from django.conf.urls import url
from django.urls.conf import path, re_path
from . import views

urlpatterns = [
    path("jobs/", views.jobs_list, name="jobs_list"),
    path("jobs/<int:id>", views.jobs_details, name="jobs_details"),
    path(
        "questionnaire/<int:id>",
        views.questionnaire_details,
        name="questionnaire_details",
    ),
    path("questionnaire/", views.questionnaire_list, name="questionnaire_list"),
]
