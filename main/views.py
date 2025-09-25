from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'crudApp1/home.html')

def form(request):
    return render(request, 'crudApp1/form.html')