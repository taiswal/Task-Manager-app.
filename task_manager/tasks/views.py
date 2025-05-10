from django.shortcuts import render,redirect,get_object_or_404
from .forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
    return render(request,'base.html')

def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list_view')
    else :
        form= TaskForm()
        return render(request,'create_view.html',{'form':form})

def update_view(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list_view')
    else:
        form=TaskForm(instance=task)
        return render(request,'update_view.html',{'form':form,'task':task})

def task_list_view(request):
    a=Task.objects.all()
    return render(request,'task_list_view.html',{'task':a})

def delete_view(request,id):
    task=Task.objects.get(id=id)
    task.delete() 
    return redirect('task_list_view')
    # return render(request,'delete_view.html')

def task_detail_view(request,id):
    task = get_object_or_404(Task,id=id)
    return render(request,'task_detail_view.html',{'task':task})