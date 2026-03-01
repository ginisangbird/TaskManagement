from django.shortcuts import render, redirect

# Store tasks in memory (no database)
tasks = []

# Function to display and add tasks
def index(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            tasks.append(task)
        return redirect("/")
    return render(request, "tasks/index.html", {"tasks": tasks})

# Function to delete a task
def delete_task(request, index):
    try:
        tasks.pop(index)
    except IndexError:
        pass
    return redirect("/")