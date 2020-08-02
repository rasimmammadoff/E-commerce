from django.forms import ModelForm, TextInput
from .models import Category

class AddCategory(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


