from comments.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "media"]

        widgets = {
            "media": forms.FileInput()
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        content_field = self.fields["content"].widget.attrs
        media_field = self.fields["media"].widget.attrs
        content_field.update({"class": "comment", })
        media_field.update({"class": "comment form-control flex", })
