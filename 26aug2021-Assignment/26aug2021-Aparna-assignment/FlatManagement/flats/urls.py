from django.urls import path
from . import views
urlpatterns = [
    path('addflat/',views.flatPage,name="flatPage"),
    path('viewallflats/',views.flats_list,name="flats_list"),
    path('viewaflat/<id>',views.flat_details,name="flat_details"),
    path('searchflat/',views.search_api,name="search_api"),
    path('updatesearchflat/',views.update_search_api,name="update_search_api"),
    path('deletesearchflat/',views.delete_search_api,name="update_search_api"),
    path('update_api/',views.update_data_read,name="update_data_read"),
    path('delete_api/',views.delete_data_read,name="delete_data_read"),



    path('home/',views.home_page,name="home_page"),
    path('register/',views.add_flat,name="add_flat"),
    path('viewall/',views.view_all,name="view_all"),
    path('search/',views.search_flat,name="search_flat"),
    path('update/',views.update_flat,name="update_flat"),
    path('delete/',views.delete_flat,name="delete_flat"),
]