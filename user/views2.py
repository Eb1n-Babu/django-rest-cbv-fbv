from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserForm
from .models import Userlist

def user_view(request):
    userlist = Userlist.objects.all()
    return render(request, 'fbvuserprofile.html', {'userlist': userlist})

def user_detail(request, pk):
    user = Userlist.objects.get(pk=pk)
    return render(request, 'fbvuser.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(user_view)
        else:
            return HttpResponse('error')
    form = UserForm()
    return render(request, 'fbvusercreate.html', {'form': form})

def user_update(request, pk):
    user = Userlist.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(user_view)
        else:
            return HttpResponse('error')
    form = UserForm(instance=user)
    return render(request, 'fbvuserupdate.html', {'form': form})

def user_delete(request, pk):
    user = Userlist.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect(user_view)
    return render(request, 'fbvuserdelete.html', {'user': user})