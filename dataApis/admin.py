from django.contrib import admin
from .models import Questionnaire, Job, Todo

# Register your models here.
admin.site.register(Questionnaire)
admin.site.register(Job)
admin.site.register(Todo)
