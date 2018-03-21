import requests
from flask import jsonify
import json
from app.models.lesson import Lesson
from app.models.group import Group

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
    groups = self.groups_to_model(r.text)
    return jsonify(groups)


  def groups_to_model(self, groups):
    data = self.prepare_json_from(groups)
    groups = []

    for groupJson in data:
      group = Group()
      group.id = int(groupJson['id'])
      group.name = groupJson['name']
      group.faculty = groupJson['faculty']
      groups.append(group)

    return groups


  def fetch_schedule(self, group):
    l = list()
    l.extend(self.schedules_to_model(self.get_schedule(group, Week.DENUMERATOR, Subgroup.FIRST)))
    l.extend(self.schedules_to_model(self.get_schedule(group, Week.NUMERATOR, Subgroup.FIRST)))
    l.extend(self.schedules_to_model(self.get_schedule(group, Week.DENUMERATOR, Subgroup.SECOND)))
    l.extend(self.schedules_to_model(self.get_schedule(group, Week.NUMERATOR, Subgroup.SECOND)))

    return jsonify(list(set(l)))


  def get_schedule(self, group, week, subgroup):
    url = f'{IFNTUNG.base_url}/api/schedules.php'
    params = {'group_id': group, 'week': week, 'subgroup': subgroup}
    r = requests.get(url, params=params)
    return r.text


  def schedules_to_model(self, schedules):
    data = self.prepare_json_from(schedules)
    lessons = []

    for scheduleJson in data:
      for lessonJson in scheduleJson['lessons']:
        lesson = Lesson()
        lesson.lessonNumber = int(lessonJson['period'])
        lesson.week = int(lessonJson['week'])
        lesson.subgroup = int(lessonJson['subgroup'])
        lesson.type = lessonJson['type']
        lesson.name = lessonJson['name']
        lesson.teacher = lessonJson['teacher']
        lesson.day = int(scheduleJson['day'])
        lessons.append(lesson)

    return lessons


  def prepare_json_from(self, input):
    # WORKAROUND to cut the UTF-8 BOM-8 symbol
    # possible bug here when accessing this file
    # from multiple streams
    with open('temp', 'w') as t:
      t.write(input)

    with open('temp', 'r', encoding='utf-8-sig') as t:
      data = json.load(t)

    return data