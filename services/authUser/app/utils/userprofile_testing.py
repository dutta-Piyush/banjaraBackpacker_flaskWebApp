import requests

url = 'http://127.0.0.1:5000/user_profile'  # Replace with your actual URL

response = requests.get(url)

# If the server returns JSON data
try:
    print(response)
    response_json = response.json()
    print('Response JSON:', response_json)
except ValueError:  # ValueError if the response is not in JSON format
    print('Response Content:', response.text)


# import requests
#
# url_login = 'http://127.0.0.1:5000/login'
# url_user_profile = 'http://127.0.0.1:5000/user_profile'
#
# # Make a login request to get the JWT token and set it as a cookie
# login_response = requests.post(url_login, json={'email': 'your_email', 'password': 'your_password'})
# jwt_cookie = login_response.cookies.get('jwt')
# print(jwt_cookie)
# # Make a subsequent request to a protected route with the JWT token in the cookies
# if jwt_cookie:
#     user_profile_response = requests.get(url_user_profile, cookies={'jwt': jwt_cookie})
#
#     # If the server returns JSON data
#     try:
#         print(user_profile_response)
#         response_json = user_profile_response.json()
#         print('Response JSON:', response_json)
#     except ValueError:  # ValueError if the response is not in JSON format
#         print('Response Content:', user_profile_response.text)
# else:
#     print('Login failed or JWT token not received')
