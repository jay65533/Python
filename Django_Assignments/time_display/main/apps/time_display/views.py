from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited

from time import gmtime, strftime
def index(request):
    context = {
        "datetime": strftime("%b %d, %Y %H:%M %p", gmtime())
    }
    return render(request,'time_display/index.html', context)