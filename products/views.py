from django.shortcuts import render
from .models import Product,Category

# home screen
def home(request):
    objects = Product.objects.all()
    men_categories = Category.objects.filter(gender='Men')
    woman_categories = Category.objects.filter(gender='Woman')
    context = {"objects":objects,"mcategories":men_categories,"wcategories":woman_categories}
    template = 'index.html'
    return render(request,template,context)

# product click
def productDetail(request,id):
    objects = Product.objects.filter(id=id)
    template = 'shop-single.html'
    context = {'objects':objects}
    return render(request,template,context)


# get category products
def categoryDetail(request,id):
    objects = Product.objects.filter(category = id)
    men_categories = Category.objects.filter(gender='Men')
    woman_categories = Category.objects.filter(gender='Woman')
    context = {"objects": objects, "mcategories": men_categories, "wcategories": woman_categories}
    template = 'index.html'
    return render(request,template,context)