from django.db import models
from tasks.models import Task
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments")
    content = models.TextField()
    creted_date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="comments/", null=True, blank=True)

    def __str__(self):
        return f"{self.author} {self.creted_date}"

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
