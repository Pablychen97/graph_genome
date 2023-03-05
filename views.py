from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ejemplo(request):
    return render(request, 'ejemplo.html')
