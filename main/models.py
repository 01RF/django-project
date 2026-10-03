from django.db import models


class TechStack(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tech_stacks = models.ManyToManyField(TechStack, related_name="projects", blank=True)
    link = models.URLField()

    def tech_stack_list(self):
        return ", ".join(t.name for t in self.tech_stacks.all())

    def __str__(self):
        return self.name


class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    summary = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Testimony(models.Model):
    full_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.full_name


class Inquiry(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"