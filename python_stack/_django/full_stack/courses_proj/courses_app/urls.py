from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('create', views.add_course),
    path('destroy', views.delete_course, name='delete'),
    path('process', views.process_delete),
]