from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from books_app import views

urlpatterns = [
    path('', include('books_app.urls')),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
