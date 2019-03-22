from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Hello World')


def new(requests):
    return HttpResponse("This is new product's section")

