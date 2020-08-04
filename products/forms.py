from django.forms import ModelForm, TextInput
from .models import Category,Product

class AddCategory(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class AddProduct(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


