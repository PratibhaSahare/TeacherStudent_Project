from django.urls import path
from  . import views

urlpatterns= [
    path("", views.Teacher_app,name="Teacher_app"),
    path("single_data", views.T_single_data, name="single_data"),
    path("all_data", views.T_all_data, name="all_data"),
]