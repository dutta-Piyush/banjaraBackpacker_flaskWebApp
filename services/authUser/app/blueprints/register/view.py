import uuid
from datetime import datetime
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from ...model import db, User


register_bp = Blueprint('register_bp', __name__)
api = Api(register_bp)


def get_current_date():
    current_date = datetime.now()
    return current_date


class RegisterResource(Resource):
    def post(self):
        form = request.json
        user = User.query.filter_by(email=form['email']).first()
        if user:
            return jsonify({'message': 'The user is already available'})
        else:
            new_user = User(
                user_id=str(uuid.uuid4()),
                first_name=form.get('first_name'),
                last_name=form.get('last_name'),
                email=form.get('email'),
                password=generate_password_hash(form.get('password')),
                address=form.get('address'),
                phone=form.get('phone_no'),
                reg_date=get_current_date()
            )
            print(new_user)
            print(new_user.email)
            try:
                db.session.add(new_user)
                db.session.commit()
                return jsonify({'message': 'The user is now registered'})
            except IntegrityError as e:
                db.session.rollback()  # Rollback the transaction in case of an error
                return jsonify({'message': f'The user is not registered. Error: {e}'})


api.add_resource(RegisterResource, '/api/register')
