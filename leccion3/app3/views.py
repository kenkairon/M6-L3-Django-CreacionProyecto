from django.shortcuts import render

def vistas1(request):
    return render(request, 'vistas1.html')

def vistas2(request):
    return render(request, 'vistas2.html')
