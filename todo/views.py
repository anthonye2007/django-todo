from django.shortcuts import render
from django.http import HttpResponse

def tasklist(request):
   return HttpResponse("A list of tasks")
