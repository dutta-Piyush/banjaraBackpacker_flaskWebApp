from flask_restful import Resource, Api
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from ...model import db, User
from ..token_auth.token_validator import token_required

edit_bp = Blueprint("edit_bp", __name__)
api = Api(edit_bp)


class EditUserResource(Resource):
    @token_required
    def put(self, decoded_token):
        print("Inside the Edit User Resource")
        # form = {
        #     "user_id": "122671a7-edf8-41e0-a00f-bfd7fb5d8e98",
        #     "first_name": "I dont know",
        #     "email": "piyush_new@gmail.com"
        # }
        form = request.json
        user = User.query.filter_by(user_id=decoded_token['user_id']).first()
        print("User ", user)
        if user:
            try:
                user.user_id = form.get('user_id', user.user_id)
                print(user.user_id)
                user.first_name = form.get('first_name', user.first_name)
                user.last_name = form.get('last_name', user.last_name)
                user.email = form.get('email', user.email)

                password = form.get('password')
                if password:
                    user.hashed_password = generate_password_hash(password)
                else:
                    user.hashed_password = user.password

                user.address = form.get('address', user.address)
                user.phone = form.get('phone', user.phone)
                user.reg_date = form.get('reg_date', user.reg_date)

                db.session.commit()
                return jsonify({'message': 'User data updated'})
            except Exception as e:
                # Handle specific exceptions if needed
                return jsonify({'error': f'Error updating user: {str(e)}'}), 500

    @token_required
    def delete(self, decoded_token):
        if decoded_token:
            user = User.query.filter_by(user_id=decoded_token).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                return jsonify({'message': 'User data updated'})
            else:
                return jsonify({'message': "User can't be deleted"})


api.add_resource(EditUserResource, '/api/edit_user')
