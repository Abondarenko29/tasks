from django.urls import path
from auth_system import views
from django.contrib.auth import views as django_views


urlpatterns = [
    path("register/", views.UserCreateView.as_view(), name="register"),
    path("update/", views.UserUpdateView.as_view(), name="user-update"),
    path("update/password/", views.PasswordUpdateView.as_view(),
         name="password-update"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", django_views.LogoutView.as_view(), name="logout"),
    path("details/<int:pk>", views.UserDetailView.as_view(),
         name="user-details"),
    path("delete/", views.UserDeleteView.as_view(), name="user-delete"),
]
