from django.urls import path,include
from . import views

urlpatterns = [
   #VIEWS
   path('add/',views.flat_view,name='flat_view'),
   path('viewflat/',views.fl_view,name='fl_view'),
   path('searchflats/',views.search_view,name='search_view'),
   path('deleteflat/',views.del_view,name='del_view'),
   path('updateflat/',views.upd_view,name='upd_view'),
  #APIS
   path('fadd/',views.flataddpage,name='flataddpage'),
   path('search/',views.searchapi,name='searchapi'),
   path('viewall/',views.flat_list,name='flat_list'),
   path('viewflats/<fetchid>',views.flat_details,name='flat_details'),
   path('updateactionapi/',views.update_data_read,name='update_data_read'),
   path('updatesearchapi/',views.updatesearchapi,name='updatesearchapi'),
   path('deletesearchapi/',views.deletesearchapi,name='deletesearchapi'),
   path('deleteactionapi/',views.delete_data_read,name='delete_data_read'),
]