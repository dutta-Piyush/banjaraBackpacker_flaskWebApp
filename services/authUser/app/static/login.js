function loginSubmit() {
                var email = document.getElementById('email');
                var password = document.getElementById('password');

                var login_form = {
                    "email" : email.value,
                    "password" : password.value
                }

                const url_str = 'http://127.0.0.1:5001/api/login';
                var url = new URL(url_str);
                var request = new Request(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(login_form)
                });
                fetch(request)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    console.log('Response ', response)
                    console.log('Response Header ', response.headers)
                    console.log('Response Cookie ', response.headers.get('Set-Cookie'))
                    console.log('Response Header Authorization', response.headers['Authorization'])
                    var message = document.getElementById('loginMessage');
                    message.innerText = response.headers['Authorization'];
                    return response.json(); // Parse the JSON content of the response
                })
                .then(data => {
//                    var message = document.getElementById('loginMessage');
//                    message.innerText = response.headers['Authorization'];
                    console.log(data['message'])
                })
                .catch(error => {
                    console.log(error);
                    // Handle errors here
                });
            }