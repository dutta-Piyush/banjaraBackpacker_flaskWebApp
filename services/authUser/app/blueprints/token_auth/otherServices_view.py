# This section is when someone tries to call from different microservice
from flask_restful import Api, Resource
from flask import request, jsonify, Blueprint

from .token_validator import token_required

tauth_bp = Blueprint('tauth_bp', __name__)
api = Api(tauth_bp)


class TauthResource(Resource):
    @token_required
    def post(self, decoded_token, error_message):
        if decoded_token:
            return decoded_token
        return jsonify({'message': error_message})

        # print('Start of the auth token page')
        # jwt_token = request.data
        # print("JWT Token for validation", jwt_token)
        # decoded_token = jwt.decode(jwt_token, Config.SECRET_KEY, algorithms='HS256')
        # print(decoded_token)
        # if decoded_token:
        #     # response = make_response()
        #     # response.headers['Authorization'] = decoded_token
        #     return jsonify({'Decoded Token': decoded_token})
        # return jsonify({'message': 'The authentication is invalid'})


api.add_resource(TauthResource, '/api/token_auth')
