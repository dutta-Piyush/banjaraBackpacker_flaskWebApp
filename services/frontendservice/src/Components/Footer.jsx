import 'bootstrap/dist/css/bootstrap.min.css';

const Footer = () => {
    return (
        <div className="fixed-bottom" style={{ backgroundColor: 'black' }}>
            <nav className="navbar navbar-expand-lg navbar-light bg-light d-flex justify-content-center">
                <nav className="navbar-brand mx-auto font-weight-bold display-8" to="/">Footer Section</nav>
            </nav>
        </div>
    );
}

export default Footer;
