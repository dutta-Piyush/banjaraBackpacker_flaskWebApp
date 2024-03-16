import jwt
from functools import wraps
from flask import request, make_response

from ...config import Config


def token_required(func):
    @wraps(func)
    def wrapper(self, *args, **kargs):
        jwt_token = request.cookies.get('token')
        # print("JWT Token inside wrapper of Blog Post Service -- ", jwt_token)
        if jwt_token:
            try:
                decoded_token = jwt.decode(jwt_token, Config.SECRET_KEY, algorithms='HS256')
                setattr(self, 'decoded_token', decoded_token)
                return func(self, *args, **kargs)
            except Exception as e:
                message = f'Error during Token decoding - {e}'
                setattr(self, 'message', message)
                return func(self, *args, **kargs)
        else:
            message = {'message': 'Token is not present'}
            response = make_response(message)
            return response
    return wrapper
