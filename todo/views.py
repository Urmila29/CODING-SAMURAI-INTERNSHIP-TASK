from django.shortcuts import render, redirect
import json
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), 'tasks.json')

def read_tasks():
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except:
        return []
    
def write_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file)

def index(request):
    tasks = read_tasks()

    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            tasks.append(task)
            write_tasks(tasks)

        return redirect('todolist')

    return render(request, 'todo/index.html', {'tasks': tasks})

def delete_task(request, task_id):
    tasks = read_tasks()

    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        write_tasks(tasks)

    return redirect('todolist')
    