from django import forms

class BuscarEquipo(forms.Form):
  team_name = forms.CharField(label="Equipo", max_length=200)