from app.university_providers.ifntung import IFNTUNG

class Provider:
  IFNTUNG = 'ifntung'

  def get(provider):
    if provider == Provider.IFNTUNG:
      return IFNTUNG()
    return None


  def all():
    return vars(Provider)