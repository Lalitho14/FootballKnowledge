class Equipo:
  def __init__(self, id, name, logo):
    self.id = id
    self.name = name
    self.logo = logo

  def __str__(self):
    return f'ID: {self.id} Name: {self.name} Logo: {self.logo}'
