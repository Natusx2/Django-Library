from django.test import TestCase
from django.urls import reverse

from books_app.models import Book


class BookViewsTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            description='Test description',
            publication_year=2024,
            genre='fiction',
            available_copies=3,
        )

    def test_catalog_filters_books_by_genre(self):
        fantasy_book = Book.objects.create(
            title='Fantasy Book',
            author='Second Author',
            publication_year=2023,
            genre='fantasy',
            available_copies=1,
        )

        response = self.client.get(reverse('index'), {'genre': 'fantasy'})

        self.assertEqual(list(response.context['books']), [fantasy_book])

    def test_book_edit_updates_book(self):
        response = self.client.post(reverse('edit_book', args=[self.book.id]), {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'cover_url': '',
            'description': 'Updated description',
            'publication_year': 2025,
            'genre': 'classic',
            'available_copies': 5,
        })

        self.book.refresh_from_db()
        self.assertRedirects(response, reverse('admin'))
        self.assertEqual(self.book.title, 'Updated Book')
        self.assertEqual(self.book.genre, 'classic')
        self.assertEqual(self.book.available_copies, 5)
