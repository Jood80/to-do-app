from django.shortcuts import render, redirect
from django.http import HttpResponse

def main(request):
    return HttpResponse('<h1>Screw me/<h1>')


def toDo(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            # save it to the db
            form.save()
        return redirect('/api/v1/todo')

    constext = {'tasks': tasks, "form": form}

    return render(request, 'tasks/list.html', constext)


def updateTask(request, PK):
    task = Task.objects.get(id=PK)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/api/v1/todo')

    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, PK):

    item = Task.objects.get(id=PK)

    if request.method == "POST":
        item.delete()
        return redirect('/api/v1/todo')

    context = {'item': item}

    return render(request, 'tasks/delete_task.html', context)
