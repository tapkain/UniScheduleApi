#!flask/bin/python
from flask import request, Blueprint
from app.providers.provider import Provider
from app import app

# Initialize blueprint
api = Blueprint('api', __name__)

@api.route('/groups')
def groups():
  r = request.args
  provider_id =  r.get('provider_id')
  p = Provider.get(provider_id)
  return p.fetch_groups()


@api.route('/schedule')
def schedule():
  r = request.args
  provider_id =  r.get('provider_id')
  group_id = r.get('group_id')
  p = Provider.get(provider_id)
  return p.fetch_schedule(group_id)



@api.route('/providers')
def providers():
  return Provider.all()