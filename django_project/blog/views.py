from django.shortcuts import render
#Below added
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')


