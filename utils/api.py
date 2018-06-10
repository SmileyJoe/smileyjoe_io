from django.http import JsonResponse


def json_success(data):
    return __json_response(data, True)


def __json_response(data, success):
    data.update({"meta": {"success": success}})
    return JsonResponse(data)
