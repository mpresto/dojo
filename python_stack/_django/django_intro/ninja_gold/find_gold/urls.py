from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money', views.process),
    path('take_bet', views.take_bet),
    path('reset', views.reset),
]