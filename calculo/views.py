from django.http import HttpResponse
from django.shortcuts import render

from calculo.models import Dados_Imc


def imc_view(request):
    context = {
        'calculo': Dados_Imc.objects.all()
        }
    return render(request,'calculo/imc.html', context)