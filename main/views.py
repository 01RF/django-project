from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInformation


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