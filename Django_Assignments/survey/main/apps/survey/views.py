from django.shortcuts import render, HttpResponse, redirect

  # the index function is called when root is visited

from time import gmtime, strftime
def index(request):
  
  cities = ["San Jose", "Seattle", "Chicago", "New York"]
  languages = ["Python", "Java", "JavaScript", "Ruby"]
  context = {
    "cities" : cities,
    "languages" : languages
  }
  return render(request, "survey/index.html", context)
  

def generate(request):
  if request.method == "POST":
    print("*"*50)
    print(request.POST)
    print("*"*50)

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['languages'] = request.POST['languages']
    request.session['comment'] = request.POST['desc']
    return redirect("/submit")

def submit(request):
  return render(request, "survey/submit.html")

def goback(request):
  if request.method == "POST":
    return redirect("/")
