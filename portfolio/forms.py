from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Project, TechStack


class AdminAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_superuser:
            raise forms.ValidationError(
                "Only admin/superuser accounts can sign in here.",
                code="invalid_login",
            )


class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ["name"]


class ProjectForm(forms.ModelForm):
    tech_stack = forms.ModelChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
        required=True,
    )

    class Meta:
        model = Project
        fields = ["name", "description", "link"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in ("name", "description", "link"):
            self.fields[f].required = True

    def save(self, commit=True):
        project = super().save(commit=commit)
        if commit:
            project.tech_stacks.set([self.cleaned_data["tech_stack"]])
        return project