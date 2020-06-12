from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('create', views.add_book),
    path('<int:id>', views.book_detail),
    path('update', views.update_book),
    path('favorite', views.add_favorite),
    path('destroy_favorite', views.remove_favorite),
    path('profile/<int:id>', views.user_detail),
]