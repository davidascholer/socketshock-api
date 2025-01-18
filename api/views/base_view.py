from django.http import HttpResponse, JsonResponse
from rest_framework import status

def denied(request):
    return HttpResponse(status=status.HTTP_403_FORBIDDEN)

def test(request):
    return HttpResponse(JsonResponse({"foo":"bar"}), status=status.HTTP_403_FORBIDDEN)
