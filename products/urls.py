from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:id>/', productDetail, name='detail'),
    path('category/<int:id>/',categoryDetail, name='category'),
]
