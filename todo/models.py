from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField()

class Note(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    note = models.CharField(max_length=1024)

