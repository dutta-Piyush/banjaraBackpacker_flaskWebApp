import jwt
import datetime
from flask_restful import Api, Resource
from werkzeug.security import check_password_hash
from flask import Blueprint, request, jsonify, make_response

from ...model import User
from ...config import Config

login_bp = Blueprint('login_bp', __name__)
api = Api(login_bp)


class LoginResource(Resource):
    def post(self):
        print('Start of the logging page')
        form = request.json
        print("Form ", form)
        if form:
            existing_user = User.query.filter_by(email=form.get('email')).first()
            print("Existing User ", existing_user)
            if existing_user:
                if form['email'] and check_password_hash(existing_user.password,
                                                         form.get('password')):

                    # Create the JWT token and send it as the response
                    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                    token_payload = {
                        'user_id': existing_user.user_id,
                        'first_name': existing_user.first_name,
                        'email': existing_user.email,
                        'exp': expiration_time
                    }
                    jwt_token = jwt.encode(token_payload, Config.SECRET_KEY, algorithm='HS256')
                    print("Logging JWT Token ", jwt_token)
                    # Create a Flask response object
                    response = make_response()
                    # Set the JWT token in the response header
                    response.headers['Authorization'] = 'Bearer ' + jwt_token
                    return response

                    # # Set the JWT token to cookies
                    # # Note: HTTP-only Cookies: HTTP-only cookies are designed to be inaccessible from JavaScript,
                    # # enhancing security by preventing XSS attacks from accessing sensitive data. However,
                    # # this also means that JavaScript running in one domain cannot directly read HTTP-only cookies
                    # # set by another domain, even with CORS headers.
                    #
                    # response = make_response(jsonify({'message': 'Login successful'}))
                    # response.set_cookie('jwt_token', jwt_token, httponly=True)
                    # return response

                else:
                    return jsonify({'message': 'Incorrect Password!'}), 404
            else:
                return jsonify({'message': 'Incorrect Email or the User doesn\'t exist!'})
        else:
            return jsonify({'message': 'Login Form is not submitted properly!'})


api.add_resource(LoginResource, '/api/login')
