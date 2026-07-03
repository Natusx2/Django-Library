from django import forms

from books_app.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'cover_url',
            'genre',
            'description',
            'publication_year',
            'available_copies',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book title',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author name',
            }),
            'cover_url': forms.URLInput(attrs={
                'class': 'form-control',
            }),
            'genre': forms.Select(attrs={
                'class': 'form-select',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Description',
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publication year',
            }),
            'available_copies': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Available copies',
            }),
        }
