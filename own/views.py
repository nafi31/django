from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Title, Item
from .forms import CreateList
from django.template import loader

def create(response):
    
    if response.method=="POST":
        form = CreateList(response.POST)
        if form.is_valid():
            name = form.cleaned_data["title"]
            n = Title(name=name)
            content = form.cleaned_data["content"]
           
            c = Item(text=content,todolist=n)
            n.save()
            c.save()
            form = CreateList()
    else:
        form = CreateList()
    return render(response, 'own/create.html', {"form":form})

def notes(request):
    data= Title.objects.all()
    tmp= loader.get_template('own/notes.html')
    context = {
        'data': data
    }
    return HttpResponse(tmp.render(context,request))
def list(request,id):
    jk = Title.objects.get(id=id)
    tmpo= loader.get_template('own/x.html')
    context = {
        'jk': jk
        }
    return HttpResponse(tmpo.render(context,request))
