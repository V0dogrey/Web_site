from django import forms
from .models import CommentsList

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = CommentsList
        fields = ['user_name', 'text']
