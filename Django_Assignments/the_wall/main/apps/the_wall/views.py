from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from apps.the_wall.models import *
from django.contrib import messages


def index(request):
    if 'first_name' not in request.session:
        request.session['first_name'] = ""
    if 'last_name' not in request.session:
        request.session['last_name'] = ""
    return render(request, "the_wall/index.html")


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

    context  = {
        "messages" : Message.objects.all(),
        "comments" : Comments.objects.all()
    }
    return render(request, "the_wall/success.html", context)

def create(request):
    if request.method == "POST":
        print(request.session['id'])
        Message.objects.create(message = request.POST['message'], user = User.objects.get(id=request.session['id']))
        request.session['message_id'] = Message.objects.get(message = request.POST['message']).id
        return redirect('/success')

def create_comment(request):
    if request.method == "POST":
        Comments.objects.create(comment = request.POST['comment'], user = User.objects.get(id=request.session['id']), message = Message.objects.get(id= request.POST['m_id']))

        return redirect("/success")

def delete_comment(request):
    if request.method == "POST":
        Comments.objects.get(id = request.POST['c_id']).delete()

        return redirect("/success")

def delete_message(request):
    if request.method == "POST":
        Message.objects.get(id = request.POST['m_id']).delete()

        return redirect("/success")

def goback(request):
    if request.method == "POST":
        request.session.clear()
        
        return redirect("/")

def edit_message(request, id):

    get_message = Message.objects.get(id=id)
    context = {
        "get_message" : get_message
    }

    return render(request, "the_wall/edit.html", context)

def update(request, id):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)
        get_message = Message.objects.get(id = id)
        print(get_message)
        get_message.message = request.POST['message']
        get_message.save()
    return redirect("/success")