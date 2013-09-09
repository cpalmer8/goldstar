from django.contrib import admin
from tasks.models import ToDoList
from tasks.models import Item

admin.site.register(ToDoList)
admin.site.register(Item)
