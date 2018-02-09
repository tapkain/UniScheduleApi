import requests
from flask import jsonify

class Week:
  NUMERATOR = 1
  DENUMERATOR = 2
  COMMON = 0


class Subgroup:
  FIRST = 1
  SECOND = 2
  COMMON = 0


class IFNTUNG:
  base_url = 'http://rozklad.nung.edu.ua/application'


  def fetch_groups(self):
    url = f'{IFNTUNG.base_url}/api/groups.php'
    r = requests.get(url)
    return r.text


  def fetch_schedule(self, group):
    s = set()
    s.add(self.schedules_to_model(self.get_schedule(group, Week.DENUMERATOR, Subgroup.FIRST)))
    s.add(self.schedules_to_model(self.get_schedule(group, Week.NUMERATOR, Subgroup.FIRST)))
    s.add(self.schedules_to_model(self.get_schedule(group, Week.DENUMERATOR, Subgroup.SECOND)))
    s.add(self.schedules_to_model(self.get_schedule(group, Week.NUMERATOR, Subgroup.SECOND)))
    return jsonify(list(s))


  def get_schedule(self, group, week, subgroup):
    url = f'{IFNTUNG.base_url}/api/schedules.php'
    params = {'group_id': group, 'week': week, 'subgroup': subgroup}
    r = requests.get(url, params=params)
    return r.text


  def schedules_to_model(self, schedules):
    return schedules