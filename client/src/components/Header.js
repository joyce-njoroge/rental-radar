import React from 'react';
import { Link } from 'react-router-dom';
import '../CSS/header.css'

function Header({ isAuthenticated,userRole }) {
  const handleLogout = () => {
    // Clear the access token from the local storage
    localStorage.removeItem('access_token');
    // Redirect to the login page after logging out
    window.location.href = '/login'; // Change this to the appropriate login page path
  };
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
         
          {isAuthenticated && (
               <Link className="navbar-brand" to="/">
               RentalRader
             </Link>
               
            )}

          <div className="collapse navbar-collapse" id="navbarNavDropdown">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link active" to="/">
                  Home
                </Link>
              </li>
             
              <li className="nav-item">
                <Link className="nav-link" to="/listings">
                  Listings
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/properties">
                  Properties
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/search">
                  Search
                </Link>
              </li>
              {/* Conditionally render the "AddProperty" link for owners */}
             {isAuthenticated && userRole === 'owner' && (
                <li className="nav-item">
                  <Link className="nav-link" to="/Addproperty">
                    Add Property
                  </Link>
                </li>
              )}
            </ul>
          </div>

          <div className="d-flex justify-content-end">
            {/* Conditionally render links based on the authentication status */}
            {!isAuthenticated && (
              <>
                <Link className="btn btn-outline-primary mx-2" to="/signup">
                  Sign Up
                </Link>
                <Link className="btn btn-outline-primary" to="/login">
                  Login
                </Link>
              </>
            )}
             {isAuthenticated && (
              <button onClick={handleLogout}>Logout</button>
            )}
          </div>

            
          
          <button
            className="navbar-toggler d-lg-none"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNavDropdown"
            aria-controls="navbarNavDropdown"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
        </div>
      </nav>
    </div>
  );
}

export default Header;
