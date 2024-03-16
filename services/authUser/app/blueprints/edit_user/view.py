import datetime

import jwt
from flask_restful import Resource, Api
from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash

from ...model import db, User
from ...config import Config
from ..token_auth.token_validator import token_required

edit_bp = Blueprint("edit_bp", __name__)
api = Api(edit_bp)


class EditUserResource(Resource):

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
                expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
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


api.add_resource(EditUserResource, '/api/edit_user')
