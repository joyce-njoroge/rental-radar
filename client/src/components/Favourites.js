import React, { useState, useEffect } from 'react';
import '../CSS/Favourites.css';

function Favorites() {
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    const fetchFavorites = async () => {
      try {
        const response = await fetch('/fav'); // Replace with your API endpoint
        if (!response.ok) {
          throw new Error('Failed to fetch favorites.');
        }
        const favoritesData = await response.json();
        setFavorites(favoritesData);
      } catch (error) {
        console.error('Error fetching favorites:', error);
      }
    };

    fetchFavorites();
  }, []);

  return (
    <div className="favorites-container">
      <h2>Favorites</h2>
      {favorites.map((property) => (
        <div key={property.id} className="property-card">
          <h4>{property.name}</h4>
          <p>{property.address}</p>
          <p>Type: {property.type}</p>
          <p>Beds: {property.beds}</p>
          <p>Bath: {property.bath}</p>
          <p>Sq. Ft.: {property.sqFt}</p>
          <p>Featured Amenities: {property.amenities}</p>
          <button>REMOVE FAVORITE</button>
          <button>START APPLICATION</button>
        </div>
      ))}
    </div>
  );
}

export default Favorites;


