from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

app_name = 'library'

from django.urls import path
from . import views
# define the urls
urlpatterns = [
    path('tasks/', views.tasks),
    path('tasks/<int:pk>/', views.task_detail),
]