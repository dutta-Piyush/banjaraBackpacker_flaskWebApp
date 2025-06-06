import jwt
import datetime
from flask_restful import Api, Resource
from werkzeug.security import check_password_hash
from flask import Blueprint, request, jsonify, make_response

from ..token_auth.token_validator import token_required

from ...model import User
from ...config import Config

login_bp = Blueprint('login_bp', __name__)
logout_bp = Blueprint('logout_bp', __name__)
api_login = Api(login_bp)
api_logout = Api(logout_bp)


class LoginResource(Resource):

    def post(self):
        form = request.json
        if form:
            existing_user = User.query.filter_by(email=form.get('email')).first()
            if existing_user:
                if form['email'] and check_password_hash(existing_user.password,
                                                         form.get('password')):
                    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5)
                    token_payload = {
                        'user_id': existing_user.user_id,
                        'user_role': existing_user.user_role,
                        'first_name': existing_user.first_name,
                        'last_name': existing_user.last_name,
                        'email': existing_user.email,
                        'address': existing_user.address,
                        'phone': existing_user.phone,
                        'reg_date': str(existing_user.reg_date),
                        'exp': expiration_time
                    }
                    jwt_token = jwt.encode(token_payload, Config.SECRET_KEY, algorithm='HS256')
                    print("JWT Token in login", jwt_token)
                    # Convert bytes to string if needed
                    if isinstance(jwt_token, bytes):
                        jwt_token = jwt_token.decode('utf-8')
                    message = {'message': f'{existing_user.first_name}, You are now logged in!'}
                    response = make_response(message)
                    response.set_cookie('token', jwt_token, expires=expiration_time, secure=False, httponly=True,
                                        samesite=None)
                    response.status_code = 200
                    return response
                else:
                    message = {'message': 'Incorrect Password!'}
                    response = make_response(message)
                    response.status_code = 401
                    return response
            else:
                message = {'message': 'Incorrect Email or the User doesn\'t exist!'}
                response = make_response(message)
                response.status_code = 401
                return response
        else:
            message = {'message': 'Login Form is not submitted properly!'}
            response = make_response(message)
            response.status_code = 401
            return response


class LogoutResource(Resource):
    @token_required
    def get(self):
        print("Inside the Logout Section")
        jwt_token = request.cookies.get('token')
        print("JWT Token in Logout", jwt_token)
        decoded_token = getattr(self, 'decoded_token', None)
        if decoded_token:
            # Create a response with an expired cookie
            message = {'message': f'{decoded_token["first_name"]}, You are now logged out!'}
            response = make_response(jsonify(message))  # jsonify({'message': 'You are logged out!'})
            print("Cookies in logout before setting to zero", response)
            response.set_cookie('token', '', expires=0)
            print("Cookies in logout after setting to zero", response)
            response.status_code = 200
            return response
        else:
            message = getattr(self, 'message', None)
            response = make_response(message)
            response.status_code = 200
            return jsonify(message)


api_login.add_resource(LoginResource, '/api/login')
api_logout.add_resource(LogoutResource, '/api/logout')

# # Set the JWT token to cookies
# # Note: HTTP-only Cookies: HTTP-only cookies are designed to be inaccessible from JavaScript,
# # enhancing security by preventing XSS attacks from accessing sensitive data. However,
# # this also means that JavaScript running in one domain cannot directly read HTTP-only cookies
# # set by another domain, even with CORS headers.


# Have to implement the logic where a user is already logged in and some other users
# wants to access the login endpoint
