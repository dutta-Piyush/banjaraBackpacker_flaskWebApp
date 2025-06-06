import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Home from './Components/Home';
import Login from './Components/Login';
import Register from './Components/Register';
import Profile from './Components/Profile';
import Logout from './Components/Logout';
import PostBlog from './Components/PostBlog';
import EditBlog from './Components/EditBlog';
import DeleteBlog from './Components/DeleteBlog';
import EditUser from './Components/EditUser';
import DeleteUser from './Components/DeleteUser';
import Xfsadf from './Components/Xfsadf';
import AuthChecker from './Components/AuthenticationChecker';
import TestHome from './Components/TestHome';


const router = createBrowserRouter([
    {
        path: '/',
        element: <Home />
    },
    {
        path: '/auth',
        element: <AuthChecker />
    },
    {
        path: '/login',
        element: <Login />
    },
    {
        path: '/register',
        element: <Register />
    },
    {
        path: '/profile',
        element: <Profile />
    },
    {
        path: '/logout',
        element: <Logout />
    },
    {
        path: '/blog',
        element: <PostBlog />
    },
    {
        path: '/edit_blog/:blogId',
        element: <EditBlog />
    },
    {
        path: '/delete_blog/:blogId',
        element: <DeleteBlog />
    },
    {
        path: '/edit_user',
        element: <EditUser />
    },
    {
        path: '/delete_user',
        element: <DeleteUser />
    },
    {
        path: '/xfsadf',
        element: <Xfsadf />
    },
    {
        path: '/testHome',
        element: <TestHome />
    }
    
]);

ReactDOM.createRoot(document.getElementById('root')).render(
    <RouterProvider router={router} />
)
