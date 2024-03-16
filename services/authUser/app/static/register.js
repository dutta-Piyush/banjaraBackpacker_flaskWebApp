function registerSubmit() {
    var first_name = document.getElementById('first_name');
    var last_name = document.getElementById('last_name');
    var email = document.getElementById('email');
    var password = document.getElementById('password');
    var confirm_password = document.getElementById('confirm_password');
    var address = document.getElementById('address');
    var phone = document.getElementById('phone');

    var register_data = {
        first_name: first_name.value,
        last_name: last_name.value,
        email: email.value,
        password: password.value,
//        confirm_password: confirm_password.value,
        address: address.value,
        phone: phone.value
    };
    console.log(register_data);

    const url_string = 'http://127.0.0.1:5001/api/register';
    var url = new URL(url_string);
    var request = new Request(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(register_data)
    });

    fetch(request)
    .then(response =>{
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(response_data =>{
        console.log(response_data)
        var message = document.getElementById('registerMessage');
        message.innerText = response_data['message']
    })
    .catch(error => {
        console.error('Error:', error);
    });
}