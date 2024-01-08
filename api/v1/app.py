#!/usr/bin/python3
"""Flask Web Application"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, resources={r'/api/v1/*': {'origins': '0.0.0.0'}})


@app.teardown_appcontext
def teardown(error):
    """Clean-up method"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """404 error"""
    response = {'error': 'Not found'}
    return jsonify(response), 404

if __name__ == '__main__':
    app.run(host=getenv('HBNB_API_HOST'),
            port=getenv('HBNB_API_PORT'),
            threaded=True)
