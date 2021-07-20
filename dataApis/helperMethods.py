from django.http.response import JsonResponse
from rest_framework import status


def convertToJson(object):
    response = {}
    response["id"] = object.id
    response["title"] = object.title
    response["technologies"] = object.technologies
    response["description"] = object.description
    response["salary"] = {"min": object.salary_min, "max": object.salary_max}
    response["type"] = object.type
    response["experience"] = {
        "min": object.experience_min,
        "max": object.experience_max,
    }
    response["category"] = object.category
    response["active"] = object.active
    response["metadata"] = {
        "createdAt": object.meta_createdAt,
        "updatedAt": object.meta_updatedAt,
        "owner": object.meta_owner,
    }
    return response


def isTypeValidityCheck(question_data):
    if question_data["type"] == "mcq":
        if question_data["options"] == []:
            return 1
        elif len(question_data["options"]) != 4:
            return 3
    else:
        if question_data["options"] != []:
            return 2
    return 0


def convertToJob(object):
    response = {}

    return response
