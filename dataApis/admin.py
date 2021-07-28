from django.contrib import admin
from .models import Questionnaire, Job, Todo, Form

# Register your models here.
admin.site.register(Questionnaire)
admin.site.register(Job)
admin.site.register(Todo)
admin.site.register(Form)
