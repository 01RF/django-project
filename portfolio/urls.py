from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
]

from django.urls import path
from . import views
 
urlpatterns = [
     path("signin/", views.AdminLoginView.as_view(), name="admin_login"),
     path("signout/", LogoutView.as_view(), name="logout"),
     path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
     path("dashboard/projects/", views.ProjectListView.as_view(), name="dashboard_projects"),
     path("dashboard/projects/create/", views.ProjectCreateView.as_view(), name="project_create"),
     path("dashboard/tech-stacks/", views.TechStackListView.as_view(), name="dashboard_techstacks"),
     path("dashboard/tech-stacks/create/", views.TechStackCreateView.as_view(), name="techstack_create"),
   ]