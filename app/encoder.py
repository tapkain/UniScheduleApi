from flask.json import JSONEncoder

class ApiJSONEncoder(JSONEncoder):
  def default(self, obj):
    if hasattr(obj, 'to_json'):
      return obj.to_json()
    return super(ApiJSONEncoder, self).default(obj)