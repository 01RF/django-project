from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, PersonalInformation, Inquiry, Testimony
from .forms import ProjectForm, InquiryForm, TestimonyForm

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