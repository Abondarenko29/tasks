from django.views.generic import UpdateView
from comments.mixins import UserIsOwnerMixin
from comments.models import Comment
from django.urls import reverse_lazy


# Create your views here.
class CommentUpdateView(UserIsOwnerMixin, UpdateView):
    model = Comment
    fields = ["content", "media"]

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.task.id})
