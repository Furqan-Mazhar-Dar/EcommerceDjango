from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)
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