import Header from "./Header";
import Footer from "./Footer";
import { useEffect, useState } from "react";
import { useNavigate, useLocation } from 'react-router-dom';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Card, Container } from 'react-bootstrap';

const Profile = () => {
    const [user, setUser] = useState('');
    const [blogs, setBlog] = useState();
    const [isLoading, setIsLoading] = useState(true);

    const navigate = useNavigate();
    const location = useLocation();

    const incomingMsg = location.state && location.state.message;


    useEffect(() => {
        const fetchData = async () => {
            const url_string = 'http://localhost:5001/api/user_profile';
            var url_profile = new URL(url_string);
            var request_profile = new Request(url_profile, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
                credentials: 'include',
            });

            fetch(request_profile)
                .then(response_profile => {
                    return response_profile.json().then(responseData_profile => ({ response_profile, responseData_profile }))
                })
                .then(({ response_profile, responseData_profile }) => {
                    if (!(response_profile.status === 200)) {
                        throw new Error(responseData_profile['message']);
                    }
                    
                    if ((response_profile.status === 200)) {
                        setUser(responseData_profile['decoded_token']);
                    }
                })
                .catch(error_profile => {
                    navigate('/login', { state: { message: error_profile.message } });
                })

            const url_blogsstring = 'http://localhost:5002/api/manage_blogs';
            var url_blogs = new URL(url_blogsstring);

            var request_blogs = new Request(url_blogs, {
                method: 'GET',
                header: {
                    'Content-Type': 'application/json'
                },
                credentials: 'include'
            });
            fetch(request_blogs)
                .then(response_blogs => {
                    return response_blogs.json().then(responseData_blogs => ({ response_blogs, responseData_blogs }))
                })
                .then(({ response_blogs, responseData_blogs }) => {
                    if (!(response_blogs.status === 200)) {
                        throw new Error(responseData_blogs['message']);
                    }
                    if (response_blogs.status === 200) {
                        setBlog(responseData_blogs['blogs_dict']);
                        setIsLoading(false);
                    }
                })
                .catch(error_blogs => {
                    console.log('Error:', error_blogs);
                });
        }        
        fetchData();
    }, [navigate]);

    return (
        <>
            <Header />
            {isLoading ? (
                <div style={{ paddingBottom: '60px', paddingTop: '150px', paddingLeft: '150px' }}><h3>Loading...</h3></div>
            ) : (
                    <div style={{ paddingBottom: '60px', paddingTop: '110px' }}>
                        <div className="container mt-5">
                            <div className="card text-center">
                                <div className="card-header">
                                    <h2>User Profile</h2>
                                </div>
                                <div className="card-body">
                                    <p className="card-text">First Name: {user.first_name}</p>
                                    <p className="card-text">Last Name: {user.last_name}</p>
                                    <p className="card-text">Email: {user.email}</p>
                                    <p className="card-text">Address: {user.address}</p>
                                    <p className="card-text">Phone: {user.phone}</p>
                                </div>
                                <Link as={Link} to="/edit_user">Edit User</Link>
                                <Link as={Link} to="/delete_user">Delete User</Link>
                            </div>
                        </div>
                        <div>
                            <Container className="mt-4" style={{ paddingBottom: '60px', paddingTop: '130px' }}>
                                <div>
                                    <p style={{ color: 'Red' }}>{ incomingMsg }</p>
                                    {blogs.map((blog, index) => (
                                        <Card key={index} className="mb-4">
                                            <Card.Body>
                                                <Card.Title> {blog.blog_id} - {blog.blog_title}</Card.Title>
                                                {/*<Card.Text>{blog.blog_body}</Card.Text>*/}
                                                <Card.Text><strong>Place:</strong> {blog.place_name}</Card.Text>
                                                <Link to={`/edit_blog/${blog.blog_id}`}>Edit</Link>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                <Link to={`/delete_blog/${blog.blog_id}`}>Delete</Link>
                                            </Card.Body>
                                        </Card>
                                    ))}
                                </div>
                            </Container>
                        </div>
                    </div>
            )}
            <Footer />
        </>
    );
};

export default Profile;
