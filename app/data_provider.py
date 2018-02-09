from app.nafta_provider import NaftaProvider

class Week:
  NUMERATOR = 1
  DENUMERATOR = 2
  COMMON = 0


class Subgroup:
  FIRST = 1
  SECOND = 2
  COMMON = 0


class Provider:
  NAFTA = 'ifntung'


def get_provider(provider):
  if provider == Provider.NAFTA:
    return NaftaProvider()
  return None