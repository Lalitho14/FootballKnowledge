import requests
from .equipo import Equipo

headers = {
    "x-rapidapi-key": "fe363def59msha69e025bf248dc5p1c6c73jsn068f274ee188",
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}


def ObtenerIdEquipo(name_team):
  url = "https://api-football-v1.p.rapidapi.com/v3/teams"
  id_teams = []
  querystring = {"search": name_team}
  response = requests.get(url, headers=headers, params=querystring)
  data = response.json()

  resultados = data['response']
  for team in resultados:
    obj = Equipo(team['team']['id'], team['team']
                 ['name'], team['team']['logo'])
    id_teams.append(obj)

  return id_teams


def ObtenerSiguientePartido(id_team):
  url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
  querystring = {"team": id_team, "next": "1"}
  response = requests.get(url, headers=headers, params=querystring)
  data = response.json()
  id_fixture = data['response'][0]['fixture']['id']
  
  return id_fixture

def Prediction(id_fixture):
  url = "https://api-football-v1.p.rapidapi.com/v3/predictions"
  querystring = {"fixture":id_fixture}
  response = requests.get(url, headers=headers, params=querystring)
  
  data = response.json()
  
  return data['response'][0]