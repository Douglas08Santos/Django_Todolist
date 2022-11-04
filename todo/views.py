from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo
# Create your views here.

def home(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos': todos
    }

    return render(request, 'todo/home.html', context)


def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']

        todo = Todo(
            title=title,
            description=description
        )
        todo.save()
        
        return redirect('/')
    else:
        return render(request, 'todo/add.html')


def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }

    return render(request, 'todo/details.html', context)



