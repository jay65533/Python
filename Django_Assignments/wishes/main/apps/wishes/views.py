from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from apps.wishes.models import *
from django.contrib import messages


def index(request):
    if 'first_name' not in request.session:
        request.session['first_name'] = ""
    if 'last_name' not in request.session:
        request.session['last_name'] = ""
    return render(request, "wishes/index.html")


def register(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)
        request.session['first_name'] = request.POST['reg_first_name']
        request.session['last_name'] = request.POST['reg_last_name']
        request.session['reg_email'] = request.POST['reg_email']
        errors = User.objects.register_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(request.POST['reg_password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name = request.POST['reg_first_name'], last_name = request.POST['reg_last_name'], email = request.POST['reg_email'], password = pw_hash)
            request.session['first_name'] = request.POST['reg_first_name']
            request.session['last_name'] = request.POST['reg_last_name']
            request.session['id'] = User.objects.get(email = request.POST['reg_email']).id
            print(request.session['first_name'])
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
            request.session['first_name'] = User.objects.get(email = request.POST['log_email']).first_name
            request.session['last_name'] = User.objects.get(email = request.POST['log_email']).last_name
            request.session['id'] = User.objects.get(email = request.POST['log_email']).id
            return redirect('/success')


def success(request):
    if 'id' not in request.session.keys():
        return redirect("/")
    
    context = {
        "wishes" : Wish.objects.all()
    }
    return render(request, "wishes/dashboard.html", context)

def create(request):
    
    return render(request, "wishes/create.html")

def create_wish(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)
        errors = User.objects.create_edit_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)
            return redirect('/success/create')
        else:
            Wish.objects.create(name = request.POST['wish'], user = User.objects.get(id=request.session['id']), granted = 0)
            return redirect("/success")

def edit_wish(request, id):

    get_wish = Wish.objects.get(id=id)
    context = {
        "get_wish" : get_wish
    }

    return render(request, "wishes/edit.html", context)

def update(request, id):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)
        errors = User.objects.create_edit_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)
            return redirect('/success/create')
        else:
            get_wish = Wish.objects.get(id = id)
            print(get_wish)
            get_wish.name = request.POST['wish']
            get_wish.save()
            return redirect("/success")

def grant(request,id):
    
    print("*"*50)
    print(request.POST)
    print("*"*50)
    get_wish = Wish.objects.get(id = id)
    print(get_wish)
    get_wish.granted = 1
    get_wish.save()
    return redirect("/success")

def goback(request):
    if request.method == "POST":
        request.session.clear()
        return redirect("/")

def destroy(request, id):

    Wish.objects.get(id=id).delete()

    return redirect("/success")
