from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render


def index(request):
    data = {
        'title': 'Departamentos',
        'subtitle': 'Listado de departamentos'
    }
    return render(request, 'index.html', data)
