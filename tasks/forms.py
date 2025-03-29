from django import forms
from tasks.models import Task, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "editors"]

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        editors_field = self.fields["editors"].widget.attrs
        name_field = self.fields["name"].widget.attrs
        editors_field.update({"rows": "10", "cols": "50",
                              "class": "form-multi-select",
                              "data-coreui-search": "true",
                              "multiple data-coreui-selection-type":
                              "counter", })
        name_field.update({"rows": "10", "cols": "50", })


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status",
                  "priority", "due_date", "maker", "project"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            field_editing = self.fields[field].widget.attrs
            field_editing.update({"rows": "10",
                                  "cols": "50", })


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("", "All")
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False,
                               label="Статус")

    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        field_status = self.fields["status"].widget.attrs
        field_status.update({"class": "form-control bg-warning"})
