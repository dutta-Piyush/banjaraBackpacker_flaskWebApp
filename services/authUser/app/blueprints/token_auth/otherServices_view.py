# This section is when someone tries to call from different microservice
from flask_restful import Api, Resource
from flask import request, jsonify, Blueprint, make_response, session

from .token_validator import token_required

tauth_bp = Blueprint('tauth_bp', __name__)
api = Api(tauth_bp)


class TauthResource(Resource):
    @token_required
    def get(self):
        decoded_token = getattr(self, 'decoded_token', None)
        message = getattr(self, 'message', None)
        if decoded_token:
            response = make_response(decoded_token)
            response.status = 200
            return response
        else:
            response = make_response(message)
            response.status = 401
            return response


api.add_resource(TauthResource, '/api/token_auth')
