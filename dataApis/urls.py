from django.conf.urls import url
from django.urls.conf import path, re_path
from . import views

urlpatterns = [
    path("jobs/", views.jobs_view, name="jobs"),
    path(
        "questionnaire/<int:id>",
        views.questionnaire_details,
        name="questionnaire_details",
    ),
    path("questionnaire/", views.questionnaire_list, name="questionnaire_list"),
]
