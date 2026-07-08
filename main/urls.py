from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.project_list, name="project_list"),
    path("projects/<int:id>/", views.project_detail, name="project_detail"),
    path("personal/", views.personal_information, name="personal_information"),
]