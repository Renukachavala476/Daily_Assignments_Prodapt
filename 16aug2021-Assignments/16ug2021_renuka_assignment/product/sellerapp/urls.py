from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.selleraddpage,name='selleraddpage'),
    path('viewall/',views.seller_list,name='seller_list'),
   
]