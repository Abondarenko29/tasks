from django.contrib.auth.models import User
from django.contrib.auth import views
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from auth_system.forms import UserCreationForm, UserUpdateForm


# Create your views here.
class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "auth_system/user_form.html"
    success_url = reverse_lazy("project-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_name"] = "Register"
        return context

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "auth_system/user_update_form.html"
    success_url = reverse_lazy("project-list")

    def get_object(self, queryset=None):
        return self.request.user


class PasswordUpdateView(LoginRequiredMixin, views.PasswordChangeView):
    template_name = "auth_system/user_form.html"
    success_url = reverse_lazy("project-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_name"] = "Update"
        return context


class CustomLoginView(views.LoginView):
    template_name = "auth_system/user_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_name"] = "Login"
        return context


class UserDetailView(DetailView):
    template_name = "auth_system/user_details.html"
    model = User
    context_object_name = "user"


class UserDeleteView(LoginRequiredMixin, DeleteView):  # Work
    template_name = "auth_system/user_delete_form.html"
    model = User
    success_url = reverse_lazy("register")

    def get_object(self, queryset=None):
        return self.request.user
