from django.http import HttpResponse

def task_lists(request):
    return HttpResponse('<h1>Todo List</h1> <p>This is your to-do list!</p>')
