from django.contrib import admin
from django.utils.html import format_html

from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','amount','price','image_field','image']
    list_filter = ['amount','price']

    def image_field(self,obj):
        return format_html('<img src="{}"  width="40px" height="40px"/>'.format(obj.image.url))
    image_field.short_description = 'Image'

admin.site.register(Product,ProductAdmin)