import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { GoogleLogin, googleLogout } from "@react-oauth/google";
import { jwtDecode } from "jwt-decode";
import Styles from './login.module.css';

const Login = () => {
    
    const navigat = useNavigate();
    const handleLogout = () => {
        console.log("user is loged out");
        googleLogout();
    }
    return (
        <div className={Styles.container}>
            <div className={Styles.loginContainer}>
                <input
                    className={Styles.input}
                    type="email"
                    placeholder="Enter your email"
                />
                <input
                    className={Styles.input}
                    type="password"
                    placeholder="Enter your password"
                />
                <button
                    className={Styles.button}
                    type="submit"
                >Login
                </button>
                <GoogleLogin
                    onSuccess={(user) => {
                        console.log(user);
                        console.log(jwtDecode(user.credential));
                        navigat("/home")

                    }}
                    onError={() => {
                        console.log("Login failed");
                    }}
                    size="Large"
                />
                {/* <button className={Styles.button} onClick={handleLogout}>Logout</button> */}
            </div>
        </div>
    )
}

export default Login;