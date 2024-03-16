import { useEffect, useState } from "react";

const AuthChecker = () => {
    const [authvalue, setAuthvalue] = useState();

    useEffect(() => {
        const url = new URL('http://localhost:5001/api/token_auth');
        var request = new Request(url, {
            method: 'GET',
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
                    setAuthvalue(false);
                }
                if (response.status === 200) {
                    setAuthvalue(true);

                }
            })
    }, []);

    return authvalue;
}

export default AuthChecker;