from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.

def home (request):
   # return HttpResponse ("Welcome to home page")
   return render (request,'my_templates.html')

def about(request):
    return HttpResponse ("about this page")


