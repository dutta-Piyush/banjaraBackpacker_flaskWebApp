function homeRoute(){
    url = 'http://127.0.0.1:5001/home'
    var request = new Request(url, {
        method: 'GET'
    })
    fetch(request)
}
function registerRoute(){
    url = 'http://127.0.0.1:5001/api/register'
    var request = new Request(url, {
        method: 'GET'
    })
    fetch(request)
    .then(response => response.text())
    .then(htmlContent => {
        document.open();
        document.write(htmlContent);
        document.close();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function loginRoute(){
    url = 'http://127.0.0.1:5001/api/login'
    var request = new Request(url, {
        method: 'GET'
    })
    fetch(request)
}
function logoutRoute(){
    url = 'http://127.0.0.1:5001/api/logout'
    var request = new Request(url, {
        method: 'GET'
    })
    fetch(request)
}
function userRoute(){
    url = 'http://127.0.0.1:5001/api/user_profile'
    var request = new Request(url, {
        method: 'GET'
    })
    fetch(request)
}
function editRoute(){
    url = 'http://127.0.0.1:5001/api/edit_user'
    var request = new Request(url, {
        method: 'GET'
    })
    fetch(request)
}