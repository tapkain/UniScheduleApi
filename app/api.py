#!flask/bin/python
from flask import request, Blueprint
from app.data_provider import get_provider
from app import app

# Initialize blueprint
api = Blueprint('api', __name__)

@api.route('/groups')
def groups():
  r = request.args
  provider_id =  r.get('provider_id')
  p = get_provider(provider_id)
  return p.get_groups()


@api.route('/schedule')
def schedule():
  r = request.args
  provider_id =  r.get('provider_id')
  group_id = r.get('group_id')
  week = r.get('week')
  subgroup = r.get('subgroup')
  p = get_provider(provider_id)
  return p.get_schedule(group_id, week, subgroup)