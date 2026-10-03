from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.project_list, name="project_list"),
    path("projects/<int:id>/", views.project_detail, name="project_detail"),
    path("personal/", views.personal_information, name="personal_information"),
    path("add-project/", views.add_project, name="add_project"),
    path("contact/", views.contact, name="contact"),
    path("add-testimony/", views.add_testimony, name="add_testimony"),
    path(
    "testimonies/",
    views.TestimonyListView.as_view(),
    name="testimony_list",
),
path(
    "testimonies/<int:pk>/",
    views.TestimonyDetailView.as_view(),
    name="testimony_detail",
),
]

