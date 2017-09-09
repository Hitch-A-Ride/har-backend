#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp

route_path_general = Blueprint("route_path_general", __name__)

@route_path_general.route('/', methods=['GET'])
def index():
    return response_with(resp.SUCCESS_200, value={"message": "Our API works"})


@route_path_general.route('/broadcast', methods=['POST'])
def broadcast_ride_details():
    try:
        data = request.get_json()

        return response_with(resp.SUCCESS_200, value={"data": data})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)
