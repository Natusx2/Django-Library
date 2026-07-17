from django.contrib import admin

from books_app.models import Book, BookComment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_year', 'available_copies', 'cover_image')
    list_filter = ('genre', 'publication_year')
    search_fields = ('title', 'author', 'description')
    ordering = ('title',)


admin.site.site_header = 'Library Admin'
admin.site.site_title = 'Library Admin'
admin.site.index_title = 'Library Management'


@admin.register(BookComment)
class BookCommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'name', 'created_at')
    search_fields = ('name', 'text', 'book__title')
    list_filter = ('created_at',)
