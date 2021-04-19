from django.db import models

# Create your models here.

class Todo_list(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
    return self.name


class Item(models.Model):
  todo_list = models.ForeignKey(Todo_list, on_delete=models.CASCADE)
  text = models.CharField(max_length=300)
  completed = models.BooleanField()

  def __str__(self):
    return self.text
