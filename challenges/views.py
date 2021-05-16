from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

month_dict = {
    "january":"January challenge",
    "february":"February challenge",
    "march":"March challenge",
    "april":"April challenge",
    "may":"May challenge",
    "june":"June challenge",
    "july":"July challenge",
    "august":"August challenge",
    "september":"September challenge",
    "october":"October challenge",
    "november":"November challenge",
    "december":"December challenge"
}

def index(request: HttpRequest):
    return HttpResponse("I am up for any challenge!")

def january(request):
    request
    return HttpResponse("This is the challenge for January")

def february(request):
    return HttpResponse("This is the challenge for February")

def say_hello(request, fname, lname):
    return HttpResponse("Hello " + fname + " " + lname)

def home(request):
    return render(request, "challenges/index.html", {
        "message" : "Click to view challenges",
        "months": list(month_dict.keys())
    })

def monthly_challenge_with_month_as_digit(request, month):
    if month < 0 or month > 12:
        return HttpResponseNotFound("Invalid month")
    return HttpResponse(month_dict[list(month_dict.keys())[month-1]])

def monthly_challenge(request, month):
    try:
        response = month_dict[month.lower()]
        return HttpResponse(response)
    except:
        return HttpResponseNotFound("Invalid month or no challenge found")

def add_challenge(request, month):
    return render(request, "challenges/add_challenge.html", {
        "month": month
    })


