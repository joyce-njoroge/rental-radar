import React from 'react';

function Logout() {
  const handleLogout = () => {
    // Clear the access token from the local storage
    localStorage.removeItem('access_token');
    // Redirect to the login page after logging out
    window.location.href = '/login'; // Change this to the appropriate login page path
  };

  return (
    <div>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Logout;