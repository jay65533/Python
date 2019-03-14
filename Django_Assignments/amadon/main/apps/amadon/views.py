from django.shortcuts import render, HttpResponse, redirect
from apps.amadon.models import *
# Create your views here.

def redirector(request):
    return redirect('/amadon')
def index(request):
    response = "Hello"
    get_products = Product.objects.all()
    context = {
        'products' : get_products
    }
    return render(request, "amadon/index.html", context)

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)
        get_products = Product.objects.all()

        request.session['name'] = request.POST['name']
        request.session['price'] = Product.objects.get(id=request.POST['price']).price
        request.session['quantity'] = request.POST['quantity']
        request.session['total'] = request.session['price'] * float(request.POST['quantity'])
        
        return redirect('/amadon/checkout')

def checkout(request):
    return render(request, "amadon/checkout.html")

def goback(request):
    return redirect('/amadon')