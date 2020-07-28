from django.shortcuts import render
from .models import Product,Category

# home screen
def home(request):
    objects = Product.objects.all()
    categories = Category.objects.all()
    context = {"objects":objects,"categories":categories}
    template = 'index.html'
    return render(request,template,context)

# product click
def productDetail(request,id):
    objects = Product.objects.filter(id=id)
    template = 'generic.html'
    context = {'objects':objects}
    return render(request,template,context)


# get category products
def categoryDetail(request,id):
    objects = Product.objects.filter(category = id)
    categories = Category.objects.all()
    context = {"objects":objects,"categories":categories}
    template = 'index.html'
    return render(request,template,context)