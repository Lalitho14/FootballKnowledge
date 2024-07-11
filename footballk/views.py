from django.shortcuts import render
from django.http import HttpResponse
from .forms import BuscarEquipo
from .consult import football_back

# Create your views here.


def Iniciarapp(request):
  if request.method == 'GET':
    return render(request, "index.html",{
      'form': BuscarEquipo
    })
  else:
    name = request.POST['team_name']
    result = football_back.ObtenerIdEquipo(name)
    return render(request, "search.html",{
      'teams': result
    })
    
def PredictionInfo(request, id_team):
  id_next = football_back.ObtenerSiguientePartido(id_team)
  fixture = football_back.Prediction(id_next)
  
  return render(request, "predictions.html",{
    'result':fixture
  })