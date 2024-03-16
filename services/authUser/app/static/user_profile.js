

var userProfile = document.getElementById('userProfile')

userProfile.addEventListener('click', function userView() {
        const url_string = 'http://127.0.0.1:5001/api/user_profile';
        var url = new URL(url_string);
        var request = new Request(url, {
            method: 'POST'
        });
        console.log("Request : ", request)
        fetch(request)
        .then(response => {
            if (!response.ok) {
                if (response.status === 401) {
                    // Handle 401 error
                    return response.json().then(data => {
                        throw new Error(`${response.status} : ${data.message} `);
                    });
                } else {
                    // Handle other errors
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
            }
            return response.json();
        })
        .then(response_data => {
            console.log("Response Data : ", response_data);

            var message = document.getElementById('user_id');
            message.innerText = response_data['user_id'];
            var message = document.getElementById('name');
            message.innerText = " " + response_data['first_name'] + " " + response_data['last_name'];
            var message = document.getElementById('email');
            message.innerText = response_data['email'];
            var message = document.getElementById('address');
            message.innerText = response_data['address'];
            var message = document.getElementById('phone');
            message.innerText = response_data['phone'];
            var message = document.getElementById('reg_date');
            message.innerText = response_data['reg_date'];

        })
        .catch(error => {
            var message = document.getElementById('userMessage');
            message.innerText = error.message;  // Display the specific error message
            console.log('Fetch Error:', error);
        });
});