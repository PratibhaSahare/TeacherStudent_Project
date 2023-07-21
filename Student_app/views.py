from django.shortcuts import render
from django.http import request, HttpResponse
from .models import Student

# Create your views here.

def Student_app(request):
    student_data = Student.objects.all()
    print(student_data)   
    return render (request,'Student_template.html',{"student_data":student_data})
    
def s_single_data(request):
    student_add = Student.objects.get(first_name='Shekhar')
    return render (request,'single_data.html', {"student":student_add})
    #return HttpResponse ("single_data")
    
def s_all_data(request):
    student_add = Student.objects.all()
    print(student_add)   
    return render (request,'all_data.html',{"student":student_add})