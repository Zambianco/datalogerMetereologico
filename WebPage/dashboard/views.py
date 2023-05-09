from django.shortcuts import render

def variaveis_clima(request):
    return render(request, 'varaveis_clima.html')

def index(request):
    return render(request, 'index.html')
