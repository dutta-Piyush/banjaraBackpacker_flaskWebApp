function editUserSubmit() {
    console.log('Edit User Log');

    var first_name = document.getElementById('first_name').value;
    var last_name = document.getElementById('last_name').value;
    var password = document.getElementById('password').value;
//    var confirm_password = document.getElementById('confirm_password').value;
    var address = document.getElementById('address').value;
    var phone = document.getElementById('phone').value;

    var edit_data = {
        first_name : first_name,
        last_name : last_name,
        password : password,
        address : address,
        phone : phone
    };
    console.log('Edit Form ', edit_data)
    const url_string = 'http://127.0.0.1:5001/api/edit_user';
    var url = new URL(url_string);
    var request = new Request(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(edit_data)
    });
    fetch(request)
    .then(response => {
        if (!response.ok){
            throw new Error('This is the 500 error which we are getting')
        }
        return response.json()
    })
    .then(response_data => {
        console.log(response_data)
    })
    .catch(error => {
        console.log('Fetch Error:', error);
    });
}