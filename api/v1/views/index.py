#!/usr/bin/python3
"""Define routes for blueprint"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def api_status():
    """Return status of application"""

    response = {'status': 'OK'}
    return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieve count of objects in storage"""
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User

    classes = {"amenities": Amenity, "cities": City,
               "places": Place, "reviews": Review,
               "states": State, "users": User}
    json_dict = {}

    for name, cls in classes.items():
        json_dict.update({name: storage.count(cls)})

    return jsonify(json_dict)
