# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [
    path('api/todos/', views.TodoList.as_view()),
    path('api/todos/<int:id>', views.TodoList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)