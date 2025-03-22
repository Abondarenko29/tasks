from django.urls import path
from comments.views import CommentUpdateView


urlpatterns = [
    path("update/<int:pk>/",
         CommentUpdateView.as_view(), name="comment-update"),
]
