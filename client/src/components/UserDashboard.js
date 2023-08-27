import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import '../CSS/UserDashboard.css';
import Profile from './Profile';
import Favorites from './Favourites';
import Logout from './Logout';

function UserDashboard() {
  const [userData, setUserData] = useState({});
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await fetch('/users'); // Replace with your API endpoint
        if (!response.ok) {
          throw new Error('Failed to fetch user data.');
        }
        const user = await response.json();
        setUserData(user);
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    };

    fetchUserData();
  }, []);

  const handleLogout = () => {
    navigate('/login');
  };

  return (
    <div className="user-dashboard">
      <div className="sidebar">
        <Link to="/profile">My Profile</Link>
        <Link to="/favourites">My Favorites</Link>
        <Logout onLogout={handleLogout} />
      </div>
    </div>
  );
}

export default UserDashboard;



