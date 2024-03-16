import uuid
from datetime import datetime
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash
from flask import Blueprint, jsonify, request, make_response

from ...model import db, User


register_bp = Blueprint('register_bp', __name__)
api = Api(register_bp)


def get_current_date():
    current_date = datetime.now()
    return current_date


class RegisterResource(Resource):

    def post(self):
        form = request.json
        print("User Form ", form)
        user = User.query.filter_by(email=form.get('email')).first()
        if user:
            message = {'message': 'The user is already available! Please login'}
            response = make_response(jsonify(message))
            response.status_code = 401
            return response
        else:
            new_user = User(
                user_id=str(uuid.uuid4()),
                user_role= 1, # form.get('user_role')
                first_name=form.get('firstName'),
                last_name=form.get('lastName'),
                email=form.get('email'),
                password=generate_password_hash(form.get('password')),
                address=form.get('address'),
                phone=int(form.get('phone')),
                reg_date=get_current_date()
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                message = {'message': 'The user is now registered'}
                return jsonify(message)
            except Exception as e:
                db.session.rollback()
                message = {'message': f'The user is not registered. Error: {e}'}
                print("Message", e)
                response = make_response(message)
                return response


api.add_resource(RegisterResource, '/api/register')
