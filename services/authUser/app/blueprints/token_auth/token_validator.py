import jwt
from functools import wraps
from flask import request, make_response, jsonify

from app.config import Config


def token_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwrgs):
        jwt_token = request.cookies.get('token')
        if jwt_token:
            try:
                decoded_token = jwt.decode(jwt_token, Config.SECRET_KEY, algorithms='HS256')
                setattr(self, 'decoded_token', decoded_token)
                return func(self, *args, **kwrgs)
            except jwt.ExpiredSignatureError:
                message = {'message': 'Token is expired'}
                setattr(self, 'message', message)
                return func(self, *args, **kwrgs)
            except jwt.InvalidTokenError:
                message = {'message': 'Invalid Token'}
                setattr(self, 'message', message)
                return func(self, *args, **kwrgs)
        else:
            message = {'message': 'Please Login!'}
            response = make_response(jsonify(message))
            response.status_code = 401
            return response
    return wrapper
