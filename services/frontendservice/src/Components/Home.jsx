import { useState, useEffect } from 'react';
import Header from './Header';
import Footer from './Footer';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Card, Container } from 'react-bootstrap';

function Home() {
    const [blogData, setBlogData] = useState([]);

    useEffect(() => {
        const url_string = 'http://127.0.0.1:5002/api/create_blog';
        var url = new URL(url_string);
        var request = new Request(url, {
            method: 'GET',
        });

        fetch(request)
            .then(response => response.json())
            .then(response_data => {
                setBlogData(response_data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <>
            <Header />
            <Container className="mt-4" style={{ paddingBottom: '60px', paddingTop: '130px' }}>
                <div>
                    {blogData.map((blog, index) => (
                        <Card key={index} className="mb-4">
                            <Card.Body>
                                <Card.Title>{blog.blog_title}</Card.Title>
                                <Card.Text>{blog.blog_body}</Card.Text>
                                <Card.Text><strong>Place:</strong> {blog.place_name}</Card.Text>
                            </Card.Body>
                        </Card>
                    ))}
                </div>
            </Container>
            <Footer />
        </>
    );
}

export default Home;
