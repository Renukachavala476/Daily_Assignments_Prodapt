from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name="Home"),
    path('add',views.Add,name="Add"),
    path('viewall',views.viewall,name="viewall"),
    path('search',views.search,name="search"),
    path('update',views.update,name="update"),
    path('delete',views.delete,name="delete"),
]