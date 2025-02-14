from django.shortcuts import render

from django.http import HttpResponse

def myfunction(request):
    return HttpResponse("hi there django *wink* *wink*")


def home(request):
    return HttpResponse("<h1>This is my home page<h1>")

def math(request):
    a=10+10
    return HttpResponse(a)

# Create your views here.
