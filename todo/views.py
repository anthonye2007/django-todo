from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

def tasklist(request):
    todos = Todo.objects.all()
    output = ", ".join([t.todo_text for t in todos])
    return HttpResponse(output)

def createtask(request):
    todo = Todo(todo_text="Get eggs")
    todo.save()
    output = "Created todo: %s" % todo.todo_text
    return HttpResponse(output)
