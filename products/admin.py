from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','amount','price','image']
    list_filter = ['amount','price']

admin.site.register(Product,ProductAdmin)