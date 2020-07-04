from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('?page=<int:id>', views.paginate),
    path('leadsearch', views.search),
]