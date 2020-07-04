from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('username', views.username),
    path('success', views.success),
    path('logout', views.logout)
]
