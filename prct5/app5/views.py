from django.shortcuts import render

# Create your views here.
from app5.models import test
from django.http import HttpResponse

def index(request):
    result = test.objects.all()
    output = ', '.join([q.Name for q in result])
    return HttpResponse(output)