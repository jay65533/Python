from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import datetime
  # the index function is called when root is visited


def index(request):
  context = {
    'users' : User.objects.order_by("first_name")
  }
  return render(request, "user_table/index.html", context)

