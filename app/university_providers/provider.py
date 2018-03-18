from app.university_providers.ifntung import IFNTUNG

class Provider:
  IFNTUNG = 'IFNTUNG'

  def get(provider):
    if provider == Provider.IFNTUNG:
      return IFNTUNG()
    return None


  def all():
    unis = [attr for attr in dir(Provider) if not callable(getattr(Provider, attr)) and not attr.startswith("__")]
    print('ZAL', unis)
    return unis