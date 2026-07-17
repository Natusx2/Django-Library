from django.test import TestCase
from django.urls import reverse

from books_app.models import Book, BookComment


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

    def test_add_book_to_favorites_session(self):
        response = self.client.get(reverse('add_to_favorites', args=[self.book.id]))

        self.assertRedirects(response, '/favorites/')
        self.assertIn(self.book.id, self.client.session['favorite_books'])

    def test_remove_book_from_favorites_session(self):
        session = self.client.session
        session['favorite_books'] = [self.book.id]
        session.save()

        response = self.client.get(reverse('remove_from_favorites', args=[self.book.id]))

        self.assertRedirects(response, '/favorites/')
        self.assertNotIn(self.book.id, self.client.session['favorite_books'])

    def test_add_comment_to_book(self):
        response = self.client.post(reverse('add_comment', args=[self.book.id]), {
            'name': 'Reader',
            'text': 'Nice book',
        })

        self.assertRedirects(response, reverse('book_detail', args=[self.book.id]))
        self.assertEqual(BookComment.objects.count(), 1)
        self.assertEqual(BookComment.objects.first().text, 'Nice book')
