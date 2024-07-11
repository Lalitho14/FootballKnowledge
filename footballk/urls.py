from django.urls import path
from . import views

urlpatterns = [
  path('', views.Iniciarapp, name='index'),
  path('prediction/<int:id_team>', views.PredictionInfo, name='prediction')
]