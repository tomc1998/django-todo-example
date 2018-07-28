from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo, Note

def index(request):
    # First build a list of todos
    context = {'todo_list': Todo.objects.order_by('done')}
    return render(request, 'index.djhtml', context)

def view_todo(request, todo_id):
    """ View a specific TODO """
    todo = Todo.objects.get(pk=todo_id)
    context = {'todo': todo,
               'notes': todo.note_set.all()}
    return render(request, 'view-todo.djhtml', context)


def create_todo(request):
    """ Create another TODO item """
    Todo(name=request.POST.get('name'), done=False).save()
    return redirect('/todo')

def toggle_todo(request, todo_id):
    """ Toggle a todo from DONE -> TODO or TODO -> DONE """
    print("HELLO2")
    todo = Todo.objects.get(pk=todo_id)
    todo.done = not todo.done
    todo.save()
    return redirect('/todo')

def add_note(request, todo_id):
    """ Add a note to a TODO """
    note = Note(todo=Todo.objects.get(pk=todo_id), note=request.POST.get('note'))
    note.save()
    return redirect(request.POST.get('next', '/'))
