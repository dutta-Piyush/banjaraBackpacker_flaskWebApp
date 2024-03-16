import { Link } from 'react-router-dom';
import Navlink from './Navlink';
import 'bootstrap/dist/css/bootstrap.min.css';

const Header = () => {


    return (
        // className="fixed-top"
        <div className="fixed-top">
            <nav className="navbar navbar-expand-lg navbar-light bg-light d-flex justify-content-center">
                <Link className="navbar-brand mx-auto font-weight-bold display-8" to="/">Banjara Wanderer</Link>
            </nav>

            <Navlink />
        </div>
    );
};
export default Header