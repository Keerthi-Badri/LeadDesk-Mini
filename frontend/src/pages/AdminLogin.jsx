import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";


function AdminLogin() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const navigate = useNavigate();


    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const response = await API.post(
                "/api/admin/login",
                {
                    email,
                    password
                }
            );


            localStorage.setItem(
                "token",
                response.data.token
            );


            navigate("/admin");


        } catch(error) {

            alert("Invalid email or password");

        }

    };


    return (
        <div className="admin-login">

            <h1>Admin Login</h1>

            <form onSubmit={handleLogin}>

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e)=>setEmail(e.target.value)}
                />


                <br/>


                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e)=>setPassword(e.target.value)}
                />


                <br/>


                <button type="submit">
                    Login
                </button>

            </form>

        </div>
    );
}


export default AdminLogin;