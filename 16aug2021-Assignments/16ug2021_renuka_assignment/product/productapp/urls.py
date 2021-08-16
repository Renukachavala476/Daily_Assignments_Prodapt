from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.productaddpage,name='productaddpage'),
    path('viewall/',views.product_list,name='product_list'),
   
]