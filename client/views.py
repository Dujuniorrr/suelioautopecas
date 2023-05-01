from django.shortcuts import get_object_or_404, redirect, render
from client.models import Client
from client.forms import ClientForm

def index(request):
    client_list = Client.objects.all()
    return render(request, "client/index.html", {"client_list": client_list})

def add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClientForm()
        
    return render(request, "client/add.html", {"form": form})

def remove(request, id):
    Client.objects.get(id=id).delete()
    return redirect('index')

def edit(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClientForm(instance=client)
    
    return render(request, "client/edit.html", {"form": form})