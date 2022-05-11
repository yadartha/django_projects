from django.contrib.auth import logout
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html', {})

def logoutUser(request):
    logout(request)
    return redirect('index')







