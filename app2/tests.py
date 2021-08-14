from django.test import TestCase
from django.http import HttpResponse    

# Create your tests here.
def specific2(request):
    return HttpResponse("<h1>specific content of app2</h1>")