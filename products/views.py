from django.shortcuts import render,redirect
from .models import Product,Category
from .forms import AddCategory

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


# contact
def contact(request):
    if request.method == 'GET':
        return  render(request,'contact.html')


def addCategory(request):
    if request.method == 'GET':
        form = AddCategory()
        return render(request,'add.html',{"form":form})

    form = AddCategory(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')

