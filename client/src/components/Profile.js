import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import '../CSS/Profile.css';

function Profile({ accessToken }) {
  const [userData, setUserData] = useState({});

  useEffect(() => {
    // Fetch user details using the accessToken
    const fetchUserData = async () => {
      try {
        const response = await fetch('/get-user-details', {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        if (response.ok) {
          const data = await response.json();
          setUserData(data.user);

          console.log('User Data:', data.user);
        }
      } catch (error) {
        console.error('Error fetching user details:', error);
      }
    };

    if (accessToken) {
      fetchUserData();
    }
  }, [accessToken]);

  return (
    <div className="profile-container">
      <div className="profile-header">
        <h2>Hi, {userData.username}!</h2>
        <div className="notifications-icon">
          {/* Replace the following line with your notifications icon or button */}
          {/* For example, you can use an SVG icon or an image */}
          <button className="notifications-button">
            <img src="notifications-icon.png" alt="Notifications" />
          </button>

          {/* You can add links to notifications, messages, or alerts */}
          <div className="notifications-dropdown">
            <ul>
              <li><Link to="/notifications">Notifications</Link></li>
              <li><Link to="/messages">Messages</Link></li>
              <li><Link to="/alerts">Alerts</Link></li>
            </ul>
          </div>
        </div>
      </div>

      <div className="profile-info">
        <h3>My Profile</h3>
        <ul>
          <li><strong>Username:</strong> {userData.username}</li>
          <li><strong>Role:</strong> {userData.role}</li>
          <li><strong>Email:</strong> {userData.email}</li>
          <li><strong>Registration Date:</strong> {userData.registrationDate}</li>
        </ul>
      </div>

      <div className="profile-actions">
        <Link to="/update-account">UPDATE ACCOUNT</Link>
        <Link to="/change-username">CHANGE USERNAME</Link>
        <Link to="/change-password">CHANGE PASSWORD</Link>
      </div>
    </div>
  );
}

export default Profile;

