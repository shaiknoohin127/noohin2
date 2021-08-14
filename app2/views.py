from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def specific2(request):
    return HttpResponse("<h1>specific2 content of string return type</h1>")