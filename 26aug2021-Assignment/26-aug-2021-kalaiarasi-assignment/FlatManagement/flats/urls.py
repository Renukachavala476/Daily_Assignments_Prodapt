from django.urls import path,include
from . import views


urlpatterns = [
    
    path('adding/',views.addata,name='addata'),
    path('homescreen/',views.homepage,name='homepage'),
    path('viewallscreen/',views.viewall,name='viewall'),
    path('searchscreen/',views.searchbuildno,name='searchbuildno'),
    path('updatescreen/',views.updation,name='updatation'),
    path('deletescreen/',views.deletion,name='deletion'),

#api
    path('add/',views.addflat,name='addflat'),
    path('viewall/',views.viewall_list,name='viewall_list'),
    path('viewone/<id>',views.flat_details,name='flat_details'),
    path('search/',views.searchapi,name='searchapi'),
    path('updatesearchapi/',views.updatesearchapi,name='updatesearchapi'),
    path('updateaction/',views.updatedataread,name='updatedataread'),
    path('deletesearchapi/',views.deletesearchapi,name='deletesearchapi'),
    path('deleteaction/',views.deletedataread,name='deletedataread'),
]