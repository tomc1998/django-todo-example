from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/<int:todo_id>/', views.view_todo, name='view-todo'),
    path('create-todo', views.create_todo, name='create-todo'),
    path('toggle-todo/<int:todo_id>', views.toggle_todo, name='toggle-todo'),
    path('todos/<int:todo_id>/add-note', views.add_note, name='add-note'),
]
