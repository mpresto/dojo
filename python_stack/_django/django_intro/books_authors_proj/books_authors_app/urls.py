from django.urls import path
from . import views


urlpatterns = [
    path('books', views.book),
    path('create_book', views.process_book),
    path('books/<int:id>', views.detail_book),
    path('add_author', views.add_author),
    path('authors', views.author),
    path('create_author', views.process_author),
    path('authors/<int:id>', views.detail_author),
    path('add_book', views.add_book),
]