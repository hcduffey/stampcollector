from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('collections/', views.CollectionList.as_view(), name="collection_list"),
    path('collections/new', views.CollectionCreate.as_view(), name="collection_create"),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name="collection_detail"),
    path('collections/<int:pk>/update', views.CollectionUpdate.as_view(), name="collection_update"),
    path('collections/<int:pk>/delete', views.CollectionDelete.as_view(), name="collection_delete"),
    path('collections/<int:pk>/stamps/new', views.StampCreate.as_view(), name="stamp_create"),
    path('collections/<int:pk>/stamps/<int:stamp_pk>/', views.StampDetail.as_view(), name="stamp_detail"),
    # need to figure out how to specify a named parameter in ViewUpdate instead of pk
    # in the meantime I just switched the names of each key in the url pattern below
    path('collections/<int:col_pk>/stamps/<int:pk>/update', views.StampUpdate.as_view(), name="stamp_update"),
    path('collections/<int:pk>/stamps/<int:stamp_pk>/delete', views.StampDelete.as_view(), name="stamp_delete"),
    path('stores/', views.StoreList.as_view(), name="store_list"),
    path('stores/new', views.StoreCreate.as_view(), name="store_create"),
    path('stores/<int:pk>/', views.StoreDetail.as_view(), name="store_detail"),
    path('stores/<int:pk>/update', views.StoreUpdate.as_view(), name="store_update"),
    path('stores/<int:pk>/delete', views.StoreDelete.as_view(), name="store_delete"),
]