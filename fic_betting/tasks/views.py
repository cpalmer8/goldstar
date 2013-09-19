from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from tasks.models import ToDoList, Item
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    logged_in_user = request.user
    if logged_in_user is not None:
        latest_task_list = ToDoList.objects.filter(user=logged_in_user.id)
        context = {'latest_task_list' : latest_task_list}
        return render(request, 'tasks/index.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))

def itemlist(request, task_id):
    task = get_object_or_404(ToDoList, id=task_id)
    task_item = Item(todolist=task, listitem="Get the milk.", due_date =
           timezone.now(), done="false")
    #task_items = ToDoList.objects.all()
    #return HttpResponse(task_item.listitem)
    user = request.user
    if (user.id  == task.user_id):
        return render(request, 'tasks/itemlist.html', {
            'task' : task,
        })
    else:
        return HttpResponseRedirect(reverse('index'))

def new(request):
    return render(request, 'tasks/addlist.html')

def addlist(request):
    task = ToDoList(listname=request.POST['listname'],
            create_date=timezone.now(), user = request.user)
    task.save()
    return HttpResponseRedirect(reverse('index'))

def add(request, task_id):
    t = get_object_or_404(ToDoList, id=task_id)
    return render(request, 'tasks/detail.html', {
        'todolist' : t,
        })

def additem(request, task_id):
    t = get_object_or_404(ToDoList, id=task_id)
    due_date = request.POST['datepicker']+ " 12:03"
    item = Item(todolist=t, listitem=request.POST['listitem'], due_date=due_date, 
            done="false")
    item.save()
    return HttpResponseRedirect(reverse('itemlist', kwargs={'task_id' : t.id }))

def login_req(request):
    return render(request, 'tasks/login.html')

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
    return HttpResponseRedirect(reverse('welcome'))

def welcome(request):
    return render(request, 'tasks/welcome.html', {
        'username' : request.user,
        })

def create_user(request):
    username = password = email = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        new_login = authenticate(username=username, password=password)
        login(request, new_login)
    return HttpResponseRedirect(reverse('welcome'))

def signup(request):
    return render(request, 'tasks/signup.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def edit_item(request, task_id, item_id):
    item = get_object_or_404(Item, id=item_id)
    listitem = request.POST['item_edit']
    item.listitem = listitem
    item.save()
    to_do = ToDoList.objects.get(id=item.todolist_id)
    return HttpResponseRedirect(reverse('itemlist',
        kwargs={ 'task_id' : to_do.id }))
