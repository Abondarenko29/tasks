from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    editors = models.ManyToManyField(User, related_name="project")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                              related_name="projects")

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low",),
        ("medium", "Medium",),
        ("high", "High",),
        ("critical", "Critical",),
    ]

    title = models.CharField(max_length=175)
    description = models.TextField()
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default="todo")
    priority = models.CharField(max_length=20,
                                choices=PRIORITY_CHOICES,
                                default="")
    due_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="creations")
    maker = models.ForeignKey(User, on_delete=models.SET_NULL,
                              null=True, blank=True, related_name="tasks")
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.title
