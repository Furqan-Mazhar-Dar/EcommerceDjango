from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'shop/index.html')
def about(request):
    return HttpResponse("This is about Us page")
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