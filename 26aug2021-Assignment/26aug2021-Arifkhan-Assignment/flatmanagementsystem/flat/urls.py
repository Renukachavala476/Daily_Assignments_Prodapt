from django.urls import path,include
from .import views
urlpatterns=[
    path('add/',views.addflat,name='addflat'),
    path('viewall/',views.flat_all,name='flat_all'),
    path('view/<fetchid>',views.flat_single,name='flat_single'),
    path('search/',views.searchapi,name='searchapi'),
    path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
    path('update/',views.flatupdate,name='flatupdate'),
    path('delete/',views.flatdelete,name='flatdelete'),


    path('register/',views.registerflat,name='registerflat'),
    path('vie/',views.flatviewss,name='flatviewss'),
    path('si/',views.flatsearch,name='flatsearch'),
    
    path('update_action_api/',views.update_data_read,name='update_data_read'),
    path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
    path('delete_action_api/',views.delete_data_read,name='delete_data_read'),
]