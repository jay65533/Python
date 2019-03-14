from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import datetime
  # the index function is called when root is visited


def index(request):
  
  return render(request, "session_words/index.html")

def generate(request):
  if request.method == "POST":
    print("*"*50)
    print(request.POST)
    print("*"*50)
    curr_time = datetime.datetime.now().strftime("%b %d, %Y %H:%M %p")
    if "words" not in request.session:
      request.session["words"] = []
    
    data = {
      "word": request.POST["word"],
      "color" : request.POST["color"],
      "showbig" : request.POST['big_font'],
      "datetime": curr_time
    }


    temp_list = request.session['words']
    temp_list.append(data)
    request.session['words'] = temp_list

    return redirect("/")

def goback(request):
  if request.method == "POST":
    #clear session
    del request.session['words']
    
    return redirect("/")
