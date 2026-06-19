from django.contrib import admin
from django.urls import include, path
from books_app import views

urlpatterns = [
    path('', include('books_app.urls')),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
]
