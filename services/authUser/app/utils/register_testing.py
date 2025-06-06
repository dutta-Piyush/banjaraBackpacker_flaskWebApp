# import requests
#
# url = 'http://127.0.0.1:5000/register'  # Replace with your actual URL
#
# form_data = {
#     "first_name": "Ayush",
#     "last_name": "Vikas",
#     "email": "ayush@gmail.com",
#     "password": "snehilsnehil",
#     "address": "Siwan, Bihar",
#     "phone_no": "9162930086"
# }
#
# response = requests.post(url, json=form_data)
#
# # If the server returns JSON data
# try:
#     response_json = response.json()
#     print('Response JSON:', response_json)
# except ValueError:  # ValueError if the response is not in JSON format
#     print('Response Content:', response.text)
