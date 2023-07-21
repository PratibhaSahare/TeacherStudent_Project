from django.shortcuts import render
from django.http import request, HttpResponse
from .models import Teacher
# Create your views here.

#def Teacher_app(request):
    #return HttpResponse ("THIS IS NORMAL PAGE")
 #   return render (request,'Teacher_template.html')

def Teacher_app(request):
    teacher_data = Teacher.objects.all()
    print(teacher_data)   
    return render (request,'Teacher_template.html',{"teacher_data":teacher_data})
    
def T_single_data(request):
    teacher_add = Teacher.objects.get(first_name='Shekhar')
    return render (request,'single_data.html', {"teacher":teacher_add})
    #return HttpResponse ("single_data")
    
def T_all_data(request):
    teacher_add = Teacher.objects.all()
    print(teacher_add)   
    return render (request,'all_data.html',{"teacher_add":teacher_add})
    