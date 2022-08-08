from django.http import HttpResponse
from django.shortcuts import render
from calculo.forms import UserForm
from calculo.models import Dados_Imc


def imc_view(request):
    #Faz a primeira renderização ao acessar a página
    if request.method == "GET":
        form = UserForm()
        context = {
            'form':form
        }
        return render(request,'calculo/imc.html', context=context)
    else:
        form = UserForm(request.POST)   
        if form.is_valid():             
            imcpeso = request.POST.get('peso')
            imcalt = request.POST.get('altura')
            imc = float(imcpeso) / (float(imcalt)* float(imcalt))
            imc_final = round(imc,1)
        
                
        context = {
            'form': form,
            'imc' : imc_final
        }
        
        return render(request,'calculo/imc.html', context=context)        