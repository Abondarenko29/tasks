from django.contrib.auth.models import User
from django.contrib.auth import forms


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ("email", )


class UserUpdateForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")
