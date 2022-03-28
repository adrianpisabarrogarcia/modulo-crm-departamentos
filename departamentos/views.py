from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from departamentos.controllers.c_usuarios import registrar_usuario




def index(request):
    return render(request, 'sign-in.html')

def register(request):
    if request.method == 'POST':
        registrar_usuario(request)
        return redirect('/')
    return render(request, 'register.html')

