from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sreelekha(request):
    return HttpResponse('<h1>this is sreelekha</h1>')


def siri(request):
    return HttpResponse('<h2><b>siri is a innocent girl</b></h1>')