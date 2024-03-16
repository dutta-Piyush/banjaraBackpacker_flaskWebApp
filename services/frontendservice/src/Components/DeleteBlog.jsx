import { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

const DeleteBlog = () => {
    const { blogId } = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        var blog_id = { 'blog_id': blogId };
        console.log("Blog ID ", blogId);
        const url_string = 'http://localhost:5002/api/manage_blogs';
        const url = new URL(url_string);
        var request = new Request(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(blog_id),
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
                    navigate('/profile', { state: { message: responseData['message'] }})
                }
            })
            .catch(error => {
                console.log("Error - ", error);
            });
    }, []);

};

export default DeleteBlog;