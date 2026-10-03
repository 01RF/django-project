from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, PersonalInformation, Inquiry, Testimony
from .forms import ProjectForm, InquiryForm, TestimonyForm
from django.views.generic import ListView, DetailView

def home(request):

    personal = PersonalInformation.objects.first()

    projects = Project.objects.all()

    return render(request, "main/index.html", {
        "personal": personal,
        "projects": projects
    })


def project_list(request):

    projects = Project.objects.all()

    return render(request, "main/project_list.html", {
        "projects": projects
    })


def project_detail(request, id):

    project = get_object_or_404(Project, id=id)

    return render(request, "main/project_detail.html", {
        "project": project
    })


def personal_information(request):

    personal = PersonalInformation.objects.first()

    return render(request, "main/personal_information.html", {
        "personal": personal
    })

def add_project(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("project_list")

    else:

        form = ProjectForm()

    return render(request, "main/add_project.html", {
        "form": form
    })

def contact(request):

    if request.method == "POST":

        form = InquiryForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = InquiryForm()

    return render(request, "main/contact.html", {
        "form": form
    })

def add_testimony(request):

    if request.method == "POST":

        form = TestimonyForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = TestimonyForm()

    return render(request, "main/add_testimony.html", {
        "form": form
    })

class TestimonyListView(ListView):

    model = Testimony

    template_name = "main/testimony_list.html"

    context_object_name = "testimonies"

class TestimonyDetailView(DetailView):

    model = Testimony

    template_name = "main/testimony_detail.html"

    context_object_name = "testimony"   

    from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView
from .forms import AdminAuthenticationForm, ProjectForm, TechStackForm
from .models import Project, TechStack


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser


class AdminLoginView(LoginView):
    template_name = "portfolio/admin_login.html"
    authentication_form = AdminAuthenticationForm

    def get_success_url(self):
        return reverse_lazy("dashboard")


class DashboardView(SuperuserRequiredMixin, TemplateView):
    template_name = "portfolio/dashboard.html"


class ProjectListView(SuperuserRequiredMixin, ListView):
    model = Project
    template_name = "portfolio/dashboard_projects.html"
    context_object_name = "projects"


class TechStackListView(SuperuserRequiredMixin, ListView):
    model = TechStack
    template_name = "portfolio/dashboard_techstacks.html"
    context_object_name = "techstacks"


class ProjectCreateView(SuperuserRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = "portfolio/form.html"
    success_url = reverse_lazy("dashboard_projects")
    extra_context = {"title": "Create Project"}


class TechStackCreateView(SuperuserRequiredMixin, CreateView):
    form_class = TechStackForm
    template_name = "portfolio/form.html"
    success_url = reverse_lazy("dashboard_techstacks")
    extra_context = {"title": "Create Tech Stack"}