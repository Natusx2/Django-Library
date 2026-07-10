from django.contrib import admin

from books_app.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_year', 'available_copies', 'cover_image')
    list_filter = ('genre', 'publication_year')
    search_fields = ('title', 'author', 'description')
    ordering = ('title',)


admin.site.site_header = 'Library Admin'
admin.site.site_title = 'Library Admin'
admin.site.index_title = 'Library Management'
