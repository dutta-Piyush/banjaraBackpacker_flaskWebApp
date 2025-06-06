# from datetime import datetime
# import jwt
# from app.config import Config
#
# # jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTIyNjcxYTctZWRmOC00' \
# #             'MWUwLWEwMGYtYmZkN2ZiNWQ4ZTk4IiwiZmlyc3RfbmFtZSI6IkF5dXNoIiwiZW1haWwiOiJh' \
# #             'eXVzaEBnbWFpbC5jb20iLCJleHAiOjE3MDkyODg2MjN9.YFOSoxrFpIO9AbyVi6mHA5Si5zCYWtXaDTbZmaBS_n4'
#
# try:
#     # If the token is expired or invalid, it will throw the error and we have to catch it
#     decoded_token = jwt.decode(jwt_token, Config.SECRET_KEY, algorithms='HS256')
#     exp = decoded_token['exp']
#     current_time = datetime.utcnow().timestamp()
#     print("Current Time ", current_time, "\n Expiration Time : ", exp)
#     if current_time >= exp:
#         print("Token Expired")
#     else:
#         print("Token is still valid")
# except jwt.ExpiredSignatureError:
#     print("Token Expired inside the exception block")
# except jwt.InvalidTokenError:
#     print('Invalid token inside the exception block')
