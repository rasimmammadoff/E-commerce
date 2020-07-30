from django.contrib import admin
from django.utils.html import format_html

from .models import Product,Category


# view of admin panel

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','amount','price','image_field','created_at','updated_at']
    list_filter = ['amount','price']
    readonly_fields = ['created_at','updated_at']

    def image_field(self,obj):
        return format_html('<img src="{}"  width="40px" height="40px"/>'.format(obj.image.url))
    image_field.short_description = 'Image'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','gender','created_at','updated_at']
    list_filter = ['title']
    readonly_fields = ['created_at','updated_at']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)