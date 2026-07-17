from django import forms

from books_app.models import BookComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = BookComment
        fields = [
            'name',
            'text',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment',
            }),
        }
