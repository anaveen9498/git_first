from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Nav(request):
    return HttpResponse('<h1> im a student of Jspiders</h1>')