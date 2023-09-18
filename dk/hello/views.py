from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response,id):
    ls=ToDoList.objects.get(id=id)
   
    return render(response,'hello/list.html',{"ls":ls})



def home(response):
    return render(response,'hello/home.html',{"name":"test"})



def create(response):
    return render(response,'hello/create.html',{})