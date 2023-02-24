from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        pas1 = request.POST['pass1']
        pas2 = request.POST['pass2']
        if pas1 == pas2:
            user = User.objects.create_user(username=un, password=pas1)
            user.save()
            print('User created')
        else:
            messages.info(request, 'Passwords don\'t match')
            return redirect('credentials:register')
        return redirect('credentials:login')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pas = request.POST['password']
        user = auth.authenticate(username=un, password=pas)
        if user is not None:
            auth.login(request, user)
            return render(request, 'content.html')
        else:
            messages.info(request, 'Invalid user')
            return redirect('credentials:login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
