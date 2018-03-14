import os
from flask import Flask
from app.encoder import ApiJSONEncoder

# Initialize application
app = Flask(__name__)

from app.api import api

app.register_blueprint(api, url_prefix='/api/v1')
app.json_encoder = ApiJSONEncoder