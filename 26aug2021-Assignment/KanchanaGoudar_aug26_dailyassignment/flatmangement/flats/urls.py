from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.Addflats,name='Addflats'),
    path('views/',views.Viewflats,name='Viewflats'),
    path('search/',views.searchflats,name='searchflats'),
    path('update/',views.updateflats,name='updateflats'),
    path('delete/',views.deleteflats,name='deleteflats'),


    path('insert/',views.Insert_Flats,name='Insert_Flats'),
    path('display/',views.Display,name='Display'),
    path('displaynew/<fetchid>',views.displayflats,name='displayflats'),
    path('searchapi/',views.searchapi,name='searchapi'),
    path('update_searchapi/',views.update_searchapi,name='update_searchapi'),
    path('update_data/',views.update_data_read,name='update_data_read'),
    path('delete_searchapi/',views.delete_searchapi,name='delete_searchapi'),
    path('delete_data/',views.delete_data_read,name='delete_data_read'),
]
