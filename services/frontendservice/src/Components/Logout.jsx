import { useEffect } from "react"
import { useNavigate } from "react-router-dom";

const Logout = () => {

    const navigate = useNavigate();

    useEffect(() => {
        const url_string = 'http://localhost:5001/api/logout';
        var url = new URL(url_string);
        var request = new Request(url, {
            method: 'GET',
            credentials: 'include'
        });
        fetch(request)
            .then(response => response.json())
            .then(response_data => {
                if (response_data) {
                    console.log(response_data['message']);
                    navigate('/login', { state: { message: response_data['message'] } });
                }
            });
    }, []);

}

export default Logout;