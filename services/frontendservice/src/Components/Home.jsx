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
                console.log('API Response:', response_data);
                // Ensure we're setting an array
                if (Array.isArray(response_data)) {
                    console.log("In the if block")
                    setBlogData(response_data);
                } else if (response_data && typeof response_data === 'object') {
                    console.log("In the else if block")
                    // If it's an object, try to find the array inside it
                    const dataArray = Object.values(response_data).find(value => Array.isArray(value));
                    setBlogData(dataArray || []);
                } else {
                    console.log("In the else block")
                    console.error('Unexpected data format:', response_data);
                    setBlogData([]);
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                setBlogData([]);
            });
    }, []);

    return (
        <>
            <Header />
            <Container className="mt-4" style={{ paddingBottom: '60px', paddingTop: '130px' }}>
                    {/* <div className='col-lg-4'>
                        <img
                            src="/images/bw-image1.jpeg"
                            alt="Image 1"
                            width="220px"
                            height="160px"
                        />
                    </div> */}
                    <div className='col-lg-6'>
                        <h1>Welcome to the Daily Feed</h1>
                    </div>
                    <div className='col-lg-8'>
                        {Array.isArray(blogData) && blogData.map((blog, index) => (
                            <div className='row' key={index}>
                                <div className='col-lg-4'>
                                    <img
                                        src="/images/bw-image1.jpeg"
                                        alt="Image 1"
                                        width="220px"
                                        height="160px"
                                    />
                                </div>
                                <div>
                                    <Card className="mb-4">
                                        <Card.Body>
                                            <Card.Title>{blog.blog_title}</Card.Title>
                                            <Card.Text>{blog.blog_body}</Card.Text>
                                            <Card.Text><strong>Place:</strong> {blog.place_name}</Card.Text>
                                        </Card.Body>
                                    </Card>
                                </div>
                            </div>
                        ))}
                    </div>
            </Container>
            <Footer />
        </>
    );
}

export default Home;
