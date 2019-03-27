from django.shortcuts import render, HttpResponse, redirect
from apps.reg_login.models import *
from django.contrib import messages

def index(request):
    
    return render(request, "reg_login/index.html")

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)
        errors = User.objects.register_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(request.POST['reg_password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name = request.POST['reg_first_name'], last_name = request.POST['reg_last_name'], email = request.POST['reg_email'], password = pw_hash)
            
            return redirect('/success')

def login(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)
            return redirect('/')
        else:
            return redirect('/success')
def success(request):
    return render(request, "reg_login/success.html")