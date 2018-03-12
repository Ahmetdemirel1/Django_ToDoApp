from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as dj_login
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib import messages
from .models import ToDo



def login(request):
    title = 'Giriş Sayfası'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or password:
             messages.add_message(request, messages.INFO, ("Kullanıcı adı ve Parola Boş Bırakılamaz!"))
        user = User.objects.get(username=username)
        if not user:
            messages.add_message(request, messages.INFO, ("Kullanıcı bulunamadi!"))
        user = authenticate(username=username, password=password)
        if (user is not None):
            if user.is_active:
                dj_login(request, user)

                return redirect('home')

    return render(request, 'login.html', {'title':title})



def register(request):
    title = 'Kayit Sayfasi'
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('password2'):
             user = User.objects.create_user(username=request.POST.get('username'),email = request.POST.get('email'),password = request.POST.get('password'))
             user.save()

             return redirect('login')

    return render(request, 'register.html', {'title':title})

def home(request):
    title = 'To Do App'
    if User.is_authenticated:
        return redirect('todo')

    return render(request, 'base.html',  {'title':title})

def todo(request):
        title = 'To Do App'
        if User.is_authenticated:
            current_user = request.user
        username = User.objects.get(username=current_user.username)
        todos = ToDo.objects.filter(user=username).order_by('-published_date')
        if request.method == 'POST':
            if(request.POST.get('delete') == None):
                todo = ToDo.objects.create(user=username)
                todo.title = request.POST.get('title')
                todo.description = request.POST.get('comment')
                todo.save()
                return redirect('home')
            else:
                delete = request.POST.get('silme')
                ToDo.objects.filter(id=delete).delete()

                return redirect('home')


        return render(request, 'home.html',  {'title':title, 'todos':todos})
