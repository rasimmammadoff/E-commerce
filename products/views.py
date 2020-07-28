from django.shortcuts import render
from .models import Product

# home screen
def home(request):
    objects = Product.objects.all()
    context = {"objects":objects}
    template = 'index.html'
    return render(request,template,context)

# product click
def productDetail(request,id):
    objects = Product.objects.filter(id=id)
    template = 'generic.html'
    context = {'objects':objects}
    return render(request,template,context)