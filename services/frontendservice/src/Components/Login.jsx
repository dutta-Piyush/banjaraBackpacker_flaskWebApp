import Header from "./Header";
import Footer from "./Footer";
import { useState } from 'react';
import { useLocation } from "react-router-dom";
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const location = useLocation();
    const message2 = location.state && location.state.message;
    const delUserMessage = location.state && location.state.delUserMessage;
    const registerMessage = location.state && location.state.registerMessage;

    const navigate = useNavigate();

    const loginUser = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        setErrorMessage('');

        const loginForm = { email, password };
        console.log('Attempting login with:', { email });

        try {
            const response = await fetch('/api/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(loginForm),
                credentials: 'include',
            });

            console.log('Login response status:', response.status);
            const responseData = await response.json();
            console.log('Login response data:', responseData);

            if (!response.ok) {
                setErrorMessage(responseData.message || 'Login failed');
                throw new Error(responseData.message || 'Login failed');
            }

            console.log('Login successful, navigating to profile');
            navigate('/profile', { state: { message: responseData.message } });
        } catch (error) {
            console.error('Login error:', error);
            setErrorMessage(error.message || 'An error occurred during login');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <>
            <Header />
            <div style={{ paddingBottom: '60px', paddingTop: '130px' }}>
                <div className="container mt-5">
                    <h1 className="text-center">Login Section</h1>
                    <div className="row justify-content-center">
                        <div className="col-md-6">
                            <form onSubmit={loginUser}>
                                {errorMessage && <p style={{ color: 'Red' }}>{errorMessage}</p>}
                                {message2 && <p style={{ color: 'Red' }}>{message2}</p>}
                                {registerMessage && <p style={{ color: 'Red' }}>{registerMessage}</p>}
                                {delUserMessage && <p style={{ color: 'Red' }}>{delUserMessage}</p>}
                                <div className="form-group mb-3">
                                    <input
                                        type="email"
                                        className="form-control"
                                        id="email"
                                        placeholder="Email"
                                        autoComplete="email"
                                        required
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                        disabled={isLoading}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="password"
                                        className="form-control"
                                        id="password"
                                        placeholder="Password"
                                        required
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                        disabled={isLoading}
                                    />
                                </div>

                                <button 
                                    type="submit" 
                                    className="btn btn-primary btn-block"
                                    disabled={isLoading}
                                >
                                    {isLoading ? 'Logging in...' : 'Login'}
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <Footer />
        </>
    );
}

export default Login;