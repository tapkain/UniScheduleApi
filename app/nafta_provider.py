import requests

class NaftaProvider:
  base_url = 'http://rozklad.nung.edu.ua/application'


  def get_groups(self):
    url = f'{NaftaProvider.base_url}/api/groups.php'
    r = requests.get(url)
    return r.text


  def get_schedule(self, group, week, subgroup):
    url = f'{NaftaProvider.base_url}/api/schedules.php'
    params = {'group_id': group, 'week': week, 'subgroup': subgroup}
    r = requests.get(url, params=params)
    return r.text