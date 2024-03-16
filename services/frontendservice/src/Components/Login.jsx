import Header from "./Header";
import Footer from "./Footer";
import { useState } from 'react';
import { useLocation } from "react-router-dom";
import { useNavigate } from 'react-router-dom';

const Login = () => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const location = useLocation();

    const message2  = location.state && location.state.message;
    const delUserMessage = location.state && location.state.delUserMessage;
    const registerMessage = location.state && location.state.registerMessage;

    const navigate = useNavigate();

    const loginUser = (e) => {

        e.preventDefault();

        const loginForm = { email, password }

        const url_string = 'http://localhost:5001/api/login';
        var url = new URL(url_string);
        var request = new Request(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginForm),
            credentials: 'include',
        });

        fetch(request)
            .then(response => {
                return response.json().then(responseData => ({ response, responseData }));
            })
            .then(({ response, responseData }) => {
                if (!(response.status === 200)) {
                    setErrorMessage(responseData['message']);
                    throw new Error(responseData['message']);
                }
                if (response.status === 200) {
                    console.log("errorMessage", errorMessage);
                    console.log("message2", message2);
                    console.log("registerMessage", registerMessage);
                    console.log("delUserMessage", delUserMessage);
                    navigate('/profile', { state: { message: responseData['message'] } });
                }
                
            })
            .catch(error => {
                console.log(error);
            });
    } 

    return (
        <>
            <Header />
            <div style={{ paddingBottom: '60px', paddingTop: '130px' }}>
                <div className="container mt-5">
                    <h1 className="text-center">Login Section</h1>
                    <div className="row justify-content-center">
                        <div className="col-md-6">
                            <form onSubmit={loginUser}>
                                <p style={{ color: 'Red' }}>{errorMessage}</p>
                                <p style={{ color: 'Red' }}>{message2}</p>
                                <p style={{ color: 'Red' }}>{registerMessage}</p>
                                <p style={{ color: 'Red' }}>{delUserMessage}</p>
                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="email"
                                        placeholder="Email"
                                        autoComplete="given-name"
                                        required
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="password"
                                        placeholder="Password"
                                        required
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                    />
                                </div>

                                <button type="submit" className="btn btn-primary btn-block">Login</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <Footer />
        </>
    );
}
export default Login