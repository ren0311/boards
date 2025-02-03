from django.urls import path

from apps import views
from .views import TodoList

app_name = "todo"
urlpatterns = [
    path("/list", TodoList.as_view(), name="list"),
]
