from django.shortcuts import render, HttpResponse, redirect
from apps.restful_users.models import *
# Create your views here.
def redirector(request):
    return redirect("/users")

def index(request):
    user = User.objects.all().values()
    context = {
        'user' : user
    }
    return render(request, 'restful_users/index.html', context)

def new(request):
    return render(request, 'restful_users/new.html')

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)

        query = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])

        get_user_id = str(User.objects.last().id)

        

    return redirect("/users/" + get_user_id)

def show(request, id):

    get_user= User.objects.get(id=id)

    context = {
        'get_user': get_user
    }

    return render(request, 'restful_users/show.html', context)

def edit(request, id):
    get_user = Message.objects.get(id=id)

    context = {
        'get_user': get_user
    }
    return render(request, 'restful_users/edit.html', context)

def update(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)

        get_user = User.objects.get(id = request.POST['hidden'])
        print(get_user)
        get_user.first_name = request.POST['first_name']
        get_user.last_name = request.POST['last_name']
        get_user.email = request.POST['email']
        get_user.save()
    return redirect("/users/" + str(get_user.id))

def destroy(request, id):

    get_user = User.objects.get(id=id).delete()

    return redirect("/")

