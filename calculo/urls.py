from django.urls import path
from . views import imc_view

urlpatterns = [
    path('imc/', imc_view), #Esta URL, encaminha a requisição do usuário para a "view"
]