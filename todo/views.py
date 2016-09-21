from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

def tasklist(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html',  {'todos':todos})

def createtask(request):
    todo = Todo(todo_text="Get eggs")
    todo.save()
    output = "Created todo: %s" % todo.todo_text
    return HttpResponse(output)

def showform(request):
    return render(request, 'todo/create.html',  {})
