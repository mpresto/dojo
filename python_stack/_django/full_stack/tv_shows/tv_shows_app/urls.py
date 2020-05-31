from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('shows', views.shows_index, name='home'),
    path('shows/new', views.add_show, name='add_new'),
    path('shows/create', views.process_show, name='process'),
    path('shows/<int:id>', views.show_detail, name='detail'),
    path('shows/<int:id>/edit', views.edit_show, name='edit'),
    path('shows/<int:id>/update', views.update_show, name='update'),
    path('shows/<int:id>/destroy', views.delete_show, name='delete'),
]