from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import App
from .forms import *

def index(request):
    app = App.objects.all()
    form  = AppForm()

    if request.method =='POST':
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context ={
        'app':app,
        'form':form,
    }
    return render(request,'app/list.html',context)

def updateTask(request,pk):
    app = App.objects.get(id=pk)
    form = AppForm(instance = app)
    if request.method == 'POST':
        form = AppForm(request.POST,instance=app)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    context = {
        'form':form,
    }

    return render(request,'app/update.html',context)

def deleteTask(request,pk):
    item = App.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {
        'item':item,
            }
    return render(request,'app/delete.html',context)