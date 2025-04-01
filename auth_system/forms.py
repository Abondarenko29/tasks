from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.forms import ModelForm


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ("email", )


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
