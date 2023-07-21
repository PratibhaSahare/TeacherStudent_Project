from django.urls import path
from  . import views

urlpatterns= [
    path("", views.Student_app,name="Student_app"),
    path("single_data", views.s_single_data, name="single_data"),
    path("all_data", views.s_all_data, name="all_data"),
]