from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('process_money', views.process, name='process'),
    path('take_bet', views.take_bet, name='bet'),
    path('reset', views.reset, name='reset'),
]