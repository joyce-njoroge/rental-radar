import React from 'react';

function UserDetails({ isVisible }) {
  // If isVisible is false, return null to hide the component
  if (!isVisible) {
    return null;
  }

  return (
    <div className="user-details">
      {/* Add user details and other information here */}
      {/* For example: */}
      <h3>User Details</h3>
      <p>Favorite Properties: ...</p>
      {/* ... */}
    </div>
  );
}

export default UserDetails;