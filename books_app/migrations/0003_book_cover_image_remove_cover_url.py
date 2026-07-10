from django.db import migrations, models


def set_book_covers(apps, schema_editor):
    Book = apps.get_model('books_app', 'Book')
    covers = {
        'The Great Gatsby': 'books/the-great-gatsby.svg',
        'To Kill a Mockingbird': 'books/to-kill-a-mockingbird.svg',
        '1984': 'books/1984.svg',
        'Pride and Prejudice': 'books/pride-and-prejudice.svg',
        'The Hobbit': 'books/the-hobbit.svg',
        'Dune': 'books/dune.svg',
    }

    for title, cover in covers.items():
        Book.objects.filter(title=title).update(cover_image=cover)


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0002_book_cover_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.FileField(blank=True, null=True, upload_to='books/'),
        ),
        migrations.RunPython(set_book_covers, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='book',
            name='cover_url',
        ),
    ]
