import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Homepage from './components/Homepage';
import Listing from './components/Listing';
import Signup from './components/Signup';
import Login from './components/Login';
import Footer from './components/Footer';
import './App.css';
import Search from './components/Search';
import Tenantsignup from './components/Tenantsignup';
import Ownersignup from './components/Ownersignup';
import ProtectedRoute from './ProtectedRoute.js';
import Logout from './components/Logout';
import PropertyDetails from "./components/PropertyDetails";
import Properties from "./components/Properties";
import ListingDetails from "./components/ListingDetails";
import Favourites from './components/Favourites';
import Profile from './components/Profile';
import UserDashboard from './components/UserDashboard';


function App() {
  const [accessToken, setAccessToken] = useState('');

  const handleLogin = (token) => {
    // Save the access token when the user logs in
    setAccessToken(token);
  };

  const handleLogout = () => {
    // Remove the access token when the user logs out
    setAccessToken('');
  };

  return (
    <div className="app-container">
      <Header isAuthenticated={!!accessToken} onLogout={handleLogout} />
      <div className="main-content">
        <Routes>
        {/* <Route
            path="/"
            element={<ProtectedRoute accessToken={accessToken}><Homepage /></ProtectedRoute>}
          /> */}
          {/* Use ProtectedRoute to protect the Listing route */}
         <Route
            path="/listings"
            element={<ProtectedRoute accessToken={accessToken} ><Listing /></ProtectedRoute>}
          /> 
           <Route
            path="/properties"
            element={<ProtectedRoute accessToken={accessToken} ><Properties /></ProtectedRoute>}
          /> 
           <Route
            path="/search"
            element={<ProtectedRoute accessToken={accessToken} ><Search/></ProtectedRoute>}
          /> 


           <Route path="/" element={<Homepage />} />
          {/* <Route path="/listings" element={<Listing />} />  */}
          <Route path="/signup" element={<Signup />} />
          {/* <Route path="/ListingDetails/:id" element={<ListingDetails />} /> */}
          {/* <Route path="/properties" element={<Properties />} /> */}
          <Route path="/propertyDetails/:id" element={<PropertyDetails />} />
          <Route path="/login" element={<Login onLogin={handleLogin} />} />
          {/* <Route path="/search" element={<Search />} /> */}
          <Route path="/Tenantsignup" element={<Tenantsignup />} />
          <Route path="/Ownersignup" element={<Ownersignup />} />
          <Route path="/logout" element={<Logout />} /> 
          <Route path="/profile" element={<Profile />} />
          <Route path="/favourites" element={<Favourites />} />
          <Route path="/userdashboard" element={<UserDashboard />} />

          {/* Use the accessToken prop for ProtectedRoute */}
          <Route
            path="/protected-route"
            element={<ProtectedRoute accessToken={accessToken} />}
          />
        </Routes>
      </div>
      <Footer />
    </div>
  );
}

export default App;