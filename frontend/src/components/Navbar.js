import { useRef } from "react";
import { FaBars, FaTimes } from "react-icons/fa";
import "../App.css";

function Navbar() {
    const navRef = useRef();

    const showNavbar = () => {
        navRef.current.classList.toggle(
            "responsive_nav"
        );
    };

    return (
        <header>
            <h3>SWENG 2023 GROUP 11</h3>
            <nav ref={navRef}>
                <a href="/Dashboard">Dashboard</a>
                <a href="/Clients">Our clients</a>
                <a href="/Group">Our group members</a>
                <a href="/Project">Project specifications</a>
                <button
                    className="nav-btn nav-close-btn"
                    onClick={showNavbar}>
                    <FaTimes />
                </button>
            </nav>
            <button
                className="nav-btn"
                onClick={showNavbar}>
                <FaBars />
            </button>
        </header>
    );
}

export default Navbar;
