from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Main routes
def index(request):
    if request.method == "GET":
        # TODO: Get user and todo info from database
        todos = Todo.objects.all().order_by('text')
        users = User.objects.all()
        return render(request, 'todoapp/index.html', { 'todos': todos, 'users': users})
    elif request.method == "POST":

        try:
            userid  = request.POST['userid']
        except (KeyValueError):
            return render(request, 'todoapp/index.html', {'error': 'You must select a task owner'})


def delete(request, todo_id):
    return HttpResponse("Delete this")

def done(request, todo_id):
    return HttpResponse("Mark done")