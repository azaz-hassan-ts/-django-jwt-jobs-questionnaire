from django.http.response import JsonResponse
from rest_framework import status


def convertToJson(object):
    response = {}
    # try:
    response["id"] = object.id
    # except:
    #     print("No id exists")
    # finally:
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
        "createdAt": object.createdAt,
        "updatedAt": object.updatedAt,
        "owner": object.owner,
    }
    return response


def isTypeValidityCheck(question_data):
    if question_data["type"] == "mcq":
        if question_data["options"] == []:
            return 1
        elif len(question_data["options"]) < 2:
            return 2
        elif len(question_data["options"]) > 4:
            return 4
    else:
        if question_data["options"] != []:
            return 3
    return 0
