from django.contrib.auth.views import LogoutView
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
    path("signin/", views.AdminLoginView.as_view(), name="admin_login"),
    path("signout/", LogoutView.as_view(), name="logout"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("dashboard/projects/", views.ProjectListView.as_view(), name="dashboard_projects"),
    path("dashboard/projects/create/", views.ProjectCreateView.as_view(), name="project_create"),
    path("dashboard/tech-stacks/", views.TechStackListView.as_view(), name="dashboard_techstacks"),
    path("dashboard/tech-stacks/create/", views.TechStackCreateView.as_view(), name="techstack_create"),
]

