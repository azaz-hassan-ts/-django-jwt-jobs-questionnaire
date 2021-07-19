from django.conf.urls import url
from django.urls.conf import path, re_path
from . import views

urlpatterns = [
    path("jobs/", views.job_view, name="jobs"),
    path("questionnaire/", views.questionnaire_view, name="questionnaire"),
]
