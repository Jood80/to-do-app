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

