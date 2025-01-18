from django.http import HttpResponse, JsonResponse
from rest_framework import status

def denied(request):
    return HttpResponse(status=status.HTTP_403_FORBIDDEN)

def test(request):
    data = {
    "test": "no data",
    }
    return HttpResponse(JsonResponse(data), status=status.HTTP_200_OK)
