import { useState } from "react";
import Footer from "./Footer";
import Header from "./Header";

const PostBlog = () => {

    const [title, setTitle] = useState('');
    const [body, setBody] = useState('');
    const [place, setPlace] = useState('');

    const [status, setStatus] = useState('');

    const blogSubmit = (e) => {

        e.preventDefault();
        const blogData = { title, body, place }

        const url_string = 'http://localhost:5002/api/create_blog';
        var url = new URL(url_string);
        var request = new Request(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(blogData),
            credentials: 'include'
        });

        fetch(request)
            .then(response => {
                return response.json().then(responseData => ({ response, responseData }));
            })
            .then(({ response, responseData }) => {
                if (!(response.status === 200)) {
                    console.log(responseData);
                    throw new Error(responseData['message']);
                }
                if (response.status === 200) {
                    console.log("Blog Posted");
                    setStatus(responseData['message']);
                    setTitle('');
                    setBody('');
                    setPlace('');
                }
            })
    }

	return (
		<>
			<Header />
            <div style={{ paddingBottom: '60px', paddingTop: '130px' }}>
                <div className="container mt-5">
                    <h1 className="text-center">Blog Posting Section</h1>
                    <div className="row justify-content-center">
                        <div className="col-md-6">
                            <form onSubmit={ blogSubmit }>
                                <p style={{ color: 'Red' }}>{ status }</p>
                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="email"
                                        placeholder="Blog Title"
                                        autoComplete="given-name"
                                        required
                                        value={title}
                                        onChange={(e) => setTitle(e.target.value)}
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="password"
                                        placeholder="Write the Blog Content"
                                        required
                                        value={body}
                                        onChange={(e) => setBody( e.target.value)}
                                        
                                    />
                                </div>

                                <div className="form-group mb-3">
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="password"
                                        placeholder="Place of visit"
                                        required
                                        value={place}
                                        onChange={(e) => setPlace( e.target.value )}
                                    />
                                </div>

                                <button type="submit" className="btn btn-primary btn-block">Post the Blog</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
			<Footer />
		</>
	)


}

export default PostBlog;