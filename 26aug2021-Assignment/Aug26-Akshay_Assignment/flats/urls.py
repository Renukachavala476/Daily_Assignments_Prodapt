from django.urls import path
from . import views

urlpatterns =[
    path('add/',views.addFlat),
    path('viewall/',views.viewall),
    path('view/<id>',views.view),



    path('',views.flat,name='flat'),
    path('updateflat/',views.updateFlat,name="updateFlat"),
    path('deleteflat/',views.deleteFlat,name="deleteFlat"),
    path('viewflat/',views.viewFlat,name="viewFlat"),
    path('searchflat/',views.searchFlat,name="searchFlat"),
    path('search/',views.searchapi,name="searchapi"),
    path('update/',views.update_search,name="update_search"),
    path('update_data/',views.update_data,name='update_data'),
    path('delete/',views.delete_search,name="delete_search"),
    path('delete_data/',views.delete_data,name='delete_data'),
    
    
    
]