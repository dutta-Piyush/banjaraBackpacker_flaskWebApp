import { Navbar, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';
//import AuthChecker from './AuthenticationChecker';
import 'bootstrap/dist/css/bootstrap.min.css';

const NavLink = () => {
    //const authvalue = AuthChecker();
    return (
        <Navbar expand="lg" bg="light">
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link as={Link} to="/">Home</Nav.Link>
                    <Nav.Link as={Link} to="/register">Register</Nav.Link>
                    <Nav.Link as={Link} to="/login">Login</Nav.Link>
                    <Nav.Link as={Link} to="/profile">Profile</Nav.Link>
                    <Nav.Link as={Link} to="/blog">Blogs</Nav.Link>
                    <Nav.Link as={Link} to="/logout">Logout</Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default NavLink;
