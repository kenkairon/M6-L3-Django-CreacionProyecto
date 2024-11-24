from django.shortcuts import render

def vistas1(request):
    return render(request, 'app3/vistas1.html')

def vistas2(request):
    return render(request, 'app3/vistas2.html')
