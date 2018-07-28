from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

def index(request):
    # First build a list of todos
    todo_list = Todo.objects.order_by('done')
    context = {'todo_list': Todo.objects.order_by('done')}
    return render(request, 'index.djhtml', context)

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
