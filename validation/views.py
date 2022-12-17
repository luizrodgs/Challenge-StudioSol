import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .validatorparms import ValidatorParms
from .validatorresponse import ValidatorResponse


@csrf_exempt
def verify(request):
    if request.method == "GET":
        error = {"error": "GET Method"}
        return JsonResponse(error)
    elif request.method == "POST":
        content = json.loads(request.body.decode())
        parms = ValidatorParms.from_dict(content)
        response = ValidatorResponse(parms)
        return JsonResponse(response.final_validation_status(), safe=False)
