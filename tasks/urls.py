from django.urls import path
from tasks import views


urlpatterns = [
     path("", views.ProjectListView.as_view(), name="project-list"),
     path("project/<int:pk>/", views.TaskListView.as_view(), name="task-list"),
     path("task/<int:pk>/", views.TaskDetailView.as_view(),
          name="task-detail"),
     path("task/create/", views.TaskCreateView.as_view(), name="task-create"),
     path("project/create/", views.ProjectCreateView.as_view(),
          name="project-create"),
     path("mytasks/", views.MyTaskListView.as_view(), name="mytasks"),
     path("task/put/<int:pk>", views.TaskUpdateView.as_view(),
          name="task-update"),
     path("task/delete/<int:pk>/", views.TaskDeleteView.as_view(),
          name="delete-task")
]
