from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
# Create your views here.


def create_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'crud/index.html', {'form': form, 'user': User.objects.all()})


def update_user(request, id):
    id = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'crud/index.html', {'form': form, 'user': User.objects.all()})


def delete_user(request, id):
    id = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=id)
    if form.is_valid():
        form.delete()
    return render(request, 'crud/index.html', {'form': form, 'user': User.objects.all()})
