# from flask import Flask, jsonify, make_response
# import requests
# import jwt
# from app.config import Config
#
# app2 = Flask(__name__)
#
#
# @app2.route('/test-edit', methods=['PUT'])
# def test_logging():
#     print("Inside edit user testing")
#     jwt_token = ''
#     response = make_response()
#     response.headers['Authorization'] = jwt_token
#     print("Inside logging testing")
#     url = 'http://127.0.0.1:5000/login'  # Replace with your actual URL
#     print("url : ", url)
#     form_data = {
#         "email": "ayush@gmail.com",
#         "password": "snehilsnehil"
#     }
#     print("Form data : ", form_data)
#     try:
#         response = requests.post(url, json=form_data)
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
#     except requests.exceptions.RequestException as e:
#         print(f"Error making request: {e}")
#         return jsonify({'message': 'Logging test failed'})
#
#     if response.status_code == 200:
#         jwt_token = response.headers.get('Authorization').split('Bearer ')[1]
#         print("JWT Token", jwt_token)
#         print("Token from the other user : ", jwt_token)
#         decoded_token = jwt.decode(jwt_token, Config.SECRET_KEY, algorithms='HS256')
#         print("Decoded Token : ", decoded_token)
#         return jsonify({'message': 'Successful', 'json_data': decoded_token})
#     else:
#         print("Some kind of Error ")
#         return jsonify({'message': 'Error'})
#
#
# if __name__ == '__main__':
#     app2.run(port=5005, debug=True)