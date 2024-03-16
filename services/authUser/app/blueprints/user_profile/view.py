from flask import Blueprint, jsonify, make_response, request
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash
import datetime
import jwt

from app.blueprints.token_auth.token_validator import token_required
from ...model import db, User
from ...config import Config

userprofile_bp = Blueprint('userprofile_bp', __name__)
api = Api(userprofile_bp)


class UserProfile(Resource):

    @token_required
    def get(self):
        decoded_token = getattr(self, 'decoded_token', None)
        message = getattr(self, 'message', None)
        if decoded_token:
            user_id = decoded_token.get('user_id')
            first_name = decoded_token.get('first_name')
            # I don't think this block of code will be eve executed because we already checked
            # the token in @token_required. Verify once the whole project is completed
            if user_id is None or first_name is None:
                message = {'message': 'Data not available in token'}
                response = make_response(message)
                response.status_code = 401
                return response
            message = {'message': 'User Details sent'}
            response_data = {'decoded_token': decoded_token, 'message': message}
            response = make_response(response_data)
            response.status_code = 200
            return response
        response = make_response(jsonify(message))
        response.status_code = 401
        return response

    @token_required
    def put(self):
        form = request.json
        decoded_token = getattr(self, 'decoded_token', None)
        user = User.query.filter_by(user_id=decoded_token['user_id']).first()
        if user:
            try:
                user.user_id = user.user_id
                user.first_name = form.get('firstName', user.first_name)
                user.last_name = form.get('lastName', user.last_name)
                user.email = user.email
                password = form.get('password')
                if password:
                    user.hashed_password = generate_password_hash(password)
                else:
                    user.hashed_password = user.password

                user.address = form.get('address', user.address)
                user.phone = form.get('phone', user.phone)
                user.reg_date = user.reg_date
                expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
                token_payload = {
                    'user_id': user.user_id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'address': user.address,
                    'phone': user.phone,
                    'reg_date': str(user.reg_date),
                    'exp': expiration_time
                }
                jwt_token = jwt.encode(token_payload, Config.SECRET_KEY, algorithm='HS256')
                print("JWT Token", jwt_token)
                db.session.commit()
                message = {'message': 'User data is updated'}
                response = make_response(message)
                response.set_cookie('token', jwt_token)
                response.status_code = 200
                return response
            except Exception as e:
                message = {'message': f'This is the error while updating user data {str(e)}'}
                response = make_response(message)
                response.status_code = 401
                return response
        else:
            message = {'message': 'Error updating user'}
            response = make_response(jsonify(message))
            response.status_code = 401
            return response

    @token_required
    def delete(self):
        decoded_token = getattr(self, 'decoded_token', None)
        if decoded_token:
            user = User.query.filter_by(user_id=decoded_token).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                message = {'message': 'User deleted'}
                response = make_response(jsonify(message))
                response.set_cookie('token', '', expires=0)
                response.status_code = 200
                return response
            else:
                message = {'message': 'Error deleting user'}
                response = make_response(jsonify(message))
                response.status_code = 401
                return response


api.add_resource(UserProfile, '/api/user_profile')
