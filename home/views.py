from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404
from django.http import Http404



def home(request):
    contexto = {
        'dado':  get_object_or_404(models.DadosPessoal, pk=1),
        'nivel': range(1, 6),
    }
    return render(request, 'apresentacao.html', contexto)

