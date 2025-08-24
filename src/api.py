from flask import Blueprint, jsonify, request
from .errors import (
    InvalidDiceError,
    DiceAlreadyExistsError,
    DiceNotFoundError
)


api_bp = Blueprint("api", __name__)

dices = [
    {"numberOfSides": 6},
    {"numberOfSides": 20}
]

@api_bp.errorhandler(Exception)
def handle_api_error(error):
    response = {
        "error_message": error.message,
        "error_name" : error.__class__.__name__,
        "status_code" : 500
    }
    if isinstance(error, InvalidDiceError):
        response["status_code"] = 400
    elif isinstance(error, DiceNotFoundError):
        response["status_code"] = 404
    elif isinstance(error, DiceAlreadyExistsError):
        response["status_code"] = 409
    else:
        response["status_code"] = 500
    return jsonify(response), response["status_code"]


@api_bp.route("dices", methods=["GET"])
def handle_get_request():
    return jsonify(dices=dices)

@api_bp.route("dices", methods=["POST"])
def handle_post_request():
    try:
        payload = request.get_json()
        if not payload["numberOfSides"]:
            raise Exception
        if not payload["numberOfSides"] > 1:
            raise Exception
        new_dices = {"numberOfSides": payload["numberOfSides"]}
        if not payload["numberOfSides"] < 256:
            raise Exception
        new_dices = {"numberOfSides": payload["numberOfSides"]}
        if new_dices in dices:
            raise Exception
        dices.append(new_dices)
        return {"message": "dices created"}, 201
    except:   
        return {"message": "An Unknown Error accured"}, 500