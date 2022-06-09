from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello World</h1>')


def projects(request):
    passages = "loren ipsum hamana hamana hamana hamana hamana hamana HAMANA."
    return HttpResponse('<p>' + passages + '</p>')


def project(request, pk):
    return HttpResponse('<h2>' + 'Single Project' + ' ' + str(pk))
