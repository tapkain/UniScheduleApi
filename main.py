#!flask/bin/python
from flask import Flask, request
from data_provider import get_provider

app = Flask(__name__)


@app.route('/api/groups')
def groups():
  r = request.args
  provider_id =  r.get('provider_id')
  p = get_provider(provider_id)
  return p.get_groups()


@app.route('/api/schedule')
def schedule():
  r = request.args
  provider_id =  r.get('provider_id')
  group_id = r.get('group_id')
  week = r.get('week')
  subgroup = r.get('subgroup')
  p = get_provider(provider_id)
  return p.get_schedule(group_id, week, subgroup)


if __name__ == '__main__':
  app.run(debug=True)