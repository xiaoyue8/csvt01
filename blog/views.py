# Create your views here.
from django.http import HttpResponse


def index(req):
    return HttpResponse('<h1>hello welcome to Django</h1>')
