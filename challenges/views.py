from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.


def index(request: HttpRequest):
    return HttpResponse("I am up for any challenge!")

def january(request):
    request
    return HttpResponse("This is the challenge for January")

def february(request):
    return HttpResponse("This is the challenge for February")

def say_hello(request, fname, lname):
    return HttpResponse("Hello " + fname + " " + lname)