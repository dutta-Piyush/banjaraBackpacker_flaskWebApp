# import requests
# import jwt
# from app.config import Config
#
# url = 'http://127.0.0.1:5000/login'  # Replace with your actual URL
#
# form_data = {
#     # "email": "piyusg@gmail.com",
#     # "password": "nihalnihal"
#     "email": "ayush@gmail.com",
#     "password": "snehilsnehil"
# }
#
# response = requests.post(url, json=form_data)
# jwt_token = response.headers.get('Authorization').split('Bearer ')[1]
# decoded_token = jwt.decode(jwt_token, Config.SECRET_KEY, algorithms='HS256')
# print("Decoded Token : ", decoded_token)


from flask import Flask, jsonify
import requests
import jwt
from app.config import Config

app2 = Flask(__name__)


@app2.route('/test-logging', methods=['GET'])
def test_logging():
    print("Inside logging testing")
    url = 'http://127.0.0.1:5001/api/login'  # Replace with your actual URL
    print("url : ", url)
    form_data = {
        "email": "piyush_new@gmail.com", # "piyush_new@gmail.com" "ayush@gmail.com"
        "password": "snehilsnehil"
    }
    print("Form data : ", form_data)
    try:
        response = requests.post(url, json=form_data)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return jsonify({'message': 'Logging test failed'})

    if response.status_code == 200:
        print("Response header ", response.headers)
        jwt_token = response.headers.get('Authorization').split('Bearer ')[1]
        print("JWT Token", jwt_token)
        print("Token from the other user : ", jwt_token)
        decoded_token = jwt.decode(jwt_token, Config.SECRET_KEY, algorithms='HS256')
        print("Decoded Token : ", decoded_token)
        print("Decoded Token ID : ", decoded_token['user_id'])
        return jsonify({'message': 'Successful', 'json_data': decoded_token})
    else:
        print("Some kind of Error ")
        return jsonify({'message': 'Error'})


if __name__ == '__main__':
    app2.run(port=5004, debug=True)
