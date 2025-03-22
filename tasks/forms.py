from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            print(field)
            field_editing = self.fields[field].widget.attrs
            field_editing.update({"class": "col-auto text-body-primary"})


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
