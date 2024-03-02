from flask import Blueprint, jsonify
from flask_restful import Api, Resource

from app.blueprints.token_auth.token_validator import token_required

userprofile_bp = Blueprint('userprofile_bp', __name__)
api = Api(userprofile_bp)


class UserProfile(Resource):
    @token_required
    def get(self, decoded_token, error_message):
        if decoded_token:
            print("Decorated Token : ", decoded_token)
            user_id = decoded_token.get('user_id')
            first_name = decoded_token.get('first_name')
            # I don't think this block of code will be eve executed because we already checked
            # the token in @token_required. Verify once the whole project is completed
            if user_id is None or first_name is None:
                return jsonify({'message': 'Invalid token'}), 500  # Use a more appropriate status code

            return jsonify({
                'user_id': user_id,
                'first_name': first_name
            })
        else:
            return jsonify({'message': error_message})


api.add_resource(UserProfile, '/api/user_profile')
