from django.db import models


class Book(models.Model):
    GENRE_CHOICES = [
        ('classic', 'Classic'),
        ('fiction', 'Fiction'),
        ('dystopian', 'Dystopian'),
        ('romance', 'Romance'),
        ('fantasy', 'Fantasy'),
        ('science fiction', 'Science Fiction'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover_image = models.FileField(upload_to='books/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    publication_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    available_copies = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.author}'
