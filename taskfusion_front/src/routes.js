import MainPage from "./components/MainPage/MainPage";
import Login from "./components/Login/Login";
import Register from "./components/Register/Register";


export const publicRoutes = [
    { path: '/', Component: MainPage },
    { path: '/login', Component: Login },
    { path: '/register', Component: Register },
];