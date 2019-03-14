from django.shortcuts import render, HttpResponse, redirect
from apps.courses.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    get_courses = Course.objects.all()
    
    context = {
        "courses":get_courses
        
    }
    return render(request, "courses/index.html",context)

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            Course.objects.create(name = request.POST['name'])
            Description.objects.create(desc = request.POST['description'], moss = Course.objects.last())
            return redirect('/')

def destroy(request, id):
    get_courses = Course.objects.get(id=id)

    context = {
        "courses":get_courses
    }
    return render(request, "courses/destroy.html", context)

def delete(request):
    if request.method == 'POST':
        Course.objects.get(id = request.POST['hid']).delete()
    return redirect('/')

def nodelete(request):
    return redirect('/')

