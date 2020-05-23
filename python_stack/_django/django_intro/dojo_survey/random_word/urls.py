from django.urls import path
from . import views
app_name = "random_word"


urlpatterns = [
    path('', views.index),
    path('reset/', views.reset),
]