from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    listname = models.CharField(max_length = 200)
    create_date = models.DateTimeField('date created')
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.listname

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList)
    listitem = models.CharField(max_length = 300)
    due_date = models.DateTimeField('date due')
    done = models.BooleanField()
    def __unicode__(self):
        return self.listitem
