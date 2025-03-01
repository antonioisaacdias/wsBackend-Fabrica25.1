from django.shortcuts import render

def login(request):
    return render(request, 'frontend/login.html')

def index(request):
    return render(request, 'frontend/index.html')
