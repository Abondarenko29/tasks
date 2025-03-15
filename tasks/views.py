from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from tasks.models import Task
from tasks.forms import TaskForm


# Create your views here.
class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
