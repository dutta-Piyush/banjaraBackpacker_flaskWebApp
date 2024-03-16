import { useEffect } from 'react';
//import { useParams } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

const DeleteUser = () => {
    const navigate = useNavigate();

    useEffect(() => {
        console.log("Inside Delete User");
        const url_string = 'http://localhost:5001/api/user_profile';
        const url = new URL(url_string);
        var request = new Request(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'include',
        });

        fetch(request)
            .then(response => {
                return response.json().then(responseData => ({ response, responseData }))
            })
            .then(({ response, responseData }) => {
                if (!(response.status === 200)) {
                    throw new Error(responseData['message']);
                }
                if (response.status === 200) {
                    navigate('/login', { state: { delUserMessage: responseData['message'] } })
                }
            })
            .catch(error => {
                console.log("Error - ", error);
            });
    }, []);

};

export default DeleteUser;