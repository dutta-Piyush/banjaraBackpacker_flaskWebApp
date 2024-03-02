import jwt
from functools import wraps
from flask import request, jsonify

from app.config import Config


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwrgs):

        jwt_token = request.headers.get('Authorization').split('Bearer ')[1]

        if jwt_token:
            try:
                # If the token is expired or invalid, it will throw the error, and we have to catch it
                decoded_token = jwt.decode(jwt_token, Config.SECRET_KEY, algorithms='HS256')
                print("Decoded Token : ", decoded_token)
                return func(decoded_token, *args, **kwrgs)

            except jwt.ExpiredSignatureError:
                return None, 'Token is expired'
            except jwt.InvalidTokenError:
                return None, 'Invalid Token'

        # If no token is provided or the token is invalid, return an error
        return jsonify({'error': 'Authentication required'}), 401
    return wrapper
