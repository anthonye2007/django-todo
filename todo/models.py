from __future__ import unicode_literals

from django.db import models

class Todo(models.Model):
    todo_text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.todo_text
