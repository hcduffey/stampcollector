from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('stamps/', views.Stamp_List.as_view(), name="Stamp_List"),
    path('stamps/new', views.StampCreate.as_view(), name="stamp_create")
]