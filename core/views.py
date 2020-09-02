from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # View code here...
    return HttpResponse("Seems you are kinda lost!")

