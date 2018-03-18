#!flask/bin/python
from flask import request, Blueprint, jsonify
from app.university_providers.provider import Provider
from app import app

# Initialize blueprint
api = Blueprint('api', __name__)

@api.route('/groups')
def groups():
  r = request.args
  provider_id =  r.get('university')
  p = Provider.get(provider_id)
  return p.fetch_groups()


@api.route('/schedule')
def schedule():
  r = request.args
  provider_id =  r.get('university')
  group_id = r.get('group_id')
  p = Provider.get(provider_id)
  return p.fetch_schedule(group_id)



@api.route('/universities')
def universities():
  return jsonify(Provider.all())