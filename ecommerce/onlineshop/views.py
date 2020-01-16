from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    products =Product.objects.all()
    print(products)
    n = len(products)
    nslide = n//4 + ceil((n/4)-(n//4))
    param ={'nslide':nslide,'range':range(nslide),'product':products}
    return render(request,'shop/index.html',param)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("This is contact Us page")
def tracker(request):
    return HttpResponse("This is tracker Us page")
def search(request):
    return HttpResponse("This is search Us page")
def product(request):
    return HttpResponse("This is product Us page")
def checkout(request):
    return HttpResponse("This is checkout Us page")