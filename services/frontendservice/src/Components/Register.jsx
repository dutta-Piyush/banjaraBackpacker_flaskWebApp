import Header from "./Header";
import Footer from "./Footer";
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

const Register = () => {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [address, setAddress] = useState('');
    const [phone, setPhone] = useState('');

    const [errorMessage, setErrorMessage] = useState();

    const navigate = useNavigate();

    const registerUser = (e) => {

        e.preventDefault();
        const register_form = { firstName, lastName, email, password, address, phone }

        const url_string = 'http://127.0.0.1:5001/api/register';
        var url = new URL(url_string);
        var request = new Request(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(register_form)
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
                    navigate('/login', { state: { registerMessage: responseData['message'] } });
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
                    <h1 className="text-center">Register Section</h1>
                    <p style={{ color:'Red'} }>{errorMessage}</p>
                    <div className="row justify-content-center">
                        <div className="col-md-6">
                            <form onSubmit={registerUser}>
                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="First Name"
                                        required
                                        value={firstName}
                                        onChange={(e) => setFirstName(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Last Name"
                                        required
                                        value={lastName}
                                        onChange={(e) => setLastName(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Email"
                                        required
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Password"
                                        required
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Address"
                                        required
                                        value={address}
                                        onChange={(e) => setAddress(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Phone"
                                        required
                                        value={phone}
                                        onChange={(e) => setPhone(e.target.value)}
                                    />
                                </div>

                                <button type="submit" className="btn btn-primary btn-block">Register</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <Footer />
        </>
    );
}
export default Register