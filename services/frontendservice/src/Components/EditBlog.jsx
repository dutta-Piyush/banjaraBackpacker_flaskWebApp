import Header from "./Header";
import Footer from "./Footer";
import { useState } from 'react';
import { useParams } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

const EditBlog = () => {
    const { blogId } = useParams();
    const navigate = useNavigate();

    const [blogTitle, setBlogTitle] = useState('');
    const [blogBody, setBlogBody] = useState('');
    const [placeName, setPlaceName] = useState('');

    const blogData = { blogId, blogTitle, blogBody, placeName }

    const editBlogs = (e) => {
        console.log("Blog Data", blogData);
        e.preventDefault();
        console.log("Blog ID ", blogId);
        const url_string = 'http://localhost:5002/api/manage_blogs';
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
                    <h1 className="text-center">Edit Blog</h1>
                    <div className="row justify-content-center">
                        <div className="col-md-6">
                            <form onSubmit={editBlogs}>
                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="First Name"
                                        required
                                        value={blogTitle}
                                        onChange={(e) => setBlogTitle(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Last Name"
                                        required
                                        value={blogBody}
                                        onChange={(e) => setBlogBody(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Email"
                                        required
                                        value={placeName}
                                        onChange={(e) => setPlaceName(e.target.value)}
                                    />
                                </div>

                                <button type="submit" className="btn btn-primary btn-block">Edit Blog</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <Footer />
        </>
    )
};

export default EditBlog;