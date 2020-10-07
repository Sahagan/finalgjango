from django.shortcuts import render
from django.http import HttpResponse
from Products.models import Product 
# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})
def Products_view(request, *args, **kwargs):
    return render(request, "product.html", {})

   

