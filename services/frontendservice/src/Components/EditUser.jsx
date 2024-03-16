import Header from "./Header";
import Footer from "./Footer";
import { useState } from 'react';
import { useParams } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

const EditUser = () => {
    const { blogId } = useParams();
    const navigate = useNavigate();

    const [firstName, setFirstName] = useState();
    const [lastName, setLastName] = useState();
    const [password, setPassword] = useState();
    const [address, setAddress] = useState();
    const [phone, setPhone] = useState();

    const blogData = { firstName, lastName, password, address, phone }

    const [errorMessage, setErrorMessage] = useState();

    const editUser = (e) => {
        console.log("Blog Data", blogData);
        e.preventDefault();
        console.log("Blog ID ", blogId);
        const url_string = 'http://localhost:5001/api/user_profile';
        const url = new URL(url_string);
        var request = new Request(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(blogData),
            credentials: 'include',
        });

        fetch(request)
            .then(response => {
                return response.json().then(responseData => ({ response, responseData }))
            })
            .then(({ response, responseData }) => {
                if (!(response.status === 200)) {
                    setErrorMessage(responseData['message'])
                    throw new Error(responseData['message']);
                }
                if (response.status === 200) {
                    console.log("Inside the Delete Section", responseData['message']);
                    navigate('/profile', { state: { message: responseData['message'] } });
                }
            })
            .catch(error => {
                console.log("Error - ", error);
            });
    }

    return (
        <>
            <Header />
            <div style={{ paddingBottom: '60px', paddingTop: '130px' }}>
                <div className="container mt-5">
                    <h1 className="text-center">Edit User</h1>
                    <p style={{ color: 'Red' }}>{errorMessage}</p>
                    <div className="row justify-content-center">
                        <div className="col-md-6">
                            <form onSubmit={editUser}>
                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Update First Name"
                                        value={firstName}
                                        onChange={(e) => setFirstName(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Update Last Name"
                                        value={lastName}
                                        onChange={(e) => setLastName(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Set New Password"
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Update Address"
                                        value={address}
                                        onChange={(e) => setAddress(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Update Phone"
                                        value={phone}
                                        onChange={(e) => setPhone(e.target.value)}
                                    />
                                </div>

                                <button type="submit" className="btn btn-primary btn-block">Update</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <Footer />
        </>
    )
};

export default EditUser;