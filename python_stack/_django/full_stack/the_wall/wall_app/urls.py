from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('destroy', views.delete_message),
]