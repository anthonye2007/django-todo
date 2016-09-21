from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

def tasklist(request):
    todos = Todo.objects.all()
    output = ", ".join([t.todo_text for t in todos])
    return HttpResponse(output)
