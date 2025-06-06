import React from 'react';
import './static/testHome.css';

const TestHome = () => {
    return (
        <>
            <div>
                <div className="slide-from-top-to-bottom-container">
                <img
                        src="/images/bw-image1.jpeg"
                        alt="Image 1"
                        className={`slide-from-top-to-bottom-image ${loaded >= 1 ? 'slide-in' : ''}`}
                        style={{ transitionDelay: '0s' }} // No delay for the first image
                        width="220px"
                        height="160px"
                    />
                    <img
                        src="/images/bw-image2.jpg"
                        alt="Image 2"
                        className={`slide-from-top-to-bottom-image ${loaded >= 2 ? 'slide-in' : ''}`}
                        style={{ transitionDelay: '1s' }} // 1 second delay for the second image
                        width="220px"
                        height="160px"
                    />
                    <img
                        src="/images/bw-image3.jpg"
                        alt="Image 3"
                        className={`slide-from-top-to-bottom-image ${loaded >= 3 ? 'slide-in' : ''}`}
                        style={{ transitionDelay: '2s' }} // 2 seconds delay for the third image
                        width="220px"
                        height="160px"
                    />
                    <img
                        src="/images/bw-image4.jpg"
                        alt="Image 4"
                        className={`slide-from-top-to-bottom-image ${loaded >= 4 ? 'slide-in' : ''}`}
                        style={{ transitionDelay: '3s' }} // 3 seconds delay for the fourth image
                        width="220px"
                        height="160px"
                    />
                </div>
            </div>
        </>
    )
}

export default TestHome;