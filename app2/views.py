from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sree(request):
    return HttpResponse('<h1>this is sree</h1>')


def lekha(request):
    return HttpResponse('<h2><b>lekha is a innocent girl</b></h1>')