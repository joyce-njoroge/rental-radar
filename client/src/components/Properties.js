import React, { useEffect, useState } from 'react';
import '../CSS/Property.css'; // Import your custom CSS file
import { Link } from 'react-router-dom';
import PropertyDetails from './PropertyDetails';

function Properties() {
  const [properties, setProperties] = useState([]);
  const [favoriteProperties, setFavoriteProperties] = useState([]);

  useEffect(() => {
    fetch('/properties')
        .then(res => res.json())
        .then(data => {
          console.log('Fetched data:', data);
            if (Array.isArray(data)) {
                setProperties(data);
            } else {
                console.error('Fetched data is not an array:', data);
            }
        })
        .catch(error => {
            console.error('Error fetching properties:', error);
        });
}, []);


  const handleLikeProperty = async (property) => {
    if (favoriteProperties.some(favProperty => favProperty.id === property.id)) {
      // Unlike the property and remove it from favorites
      setFavoriteProperties(prevFavorites => prevFavorites.filter(favProperty => favProperty.id !== property.id));
      try {
        await fetch(`/fav/${property.id}`, {
          method: 'DELETE',
        });
      } catch (error) {
        console.error('Error removing property from favorites:', error);
        // Handle error if needed
      }
    } else {
      // Like the property and add it to favorites
      setFavoriteProperties(prevFavorites => [...prevFavorites, property]);
      try {
        await fetch('/fav', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ id: property.id }), // Send the listing ID in the request body
        });
      } catch (error) {
        console.error('Error adding property to favorites:', error);
        // Handle error if needed
      }
    }
  };

  return (
    <div className="custom-property-container">
      
      <div className="custom-row">
        {properties.map(property => (
          <div key={property.id} className="custom-col-md-6 custom-col-lg-4 custom-mb-4">
            <div className="custom-card custom-listing-card">
              <div className="image-container">
                <img src={property.main_image} className="custom-card-img-top custom-property-img" alt="Property" />
              </div>
              <div className="custom-card-body">
                <h5 className="custom-card-title">{property.property_title}</h5>
                <p className="custom-card-text">Rent: Kshs {property.property_rent}</p>
                <p className="custom-card-text">Location: {property.address}</p>
                <p className="custom-card-text">Utilities: {property.amenities}</p>
                <div className="card-buttons">
                  <button onClick={() => handleLikeProperty(property)}>
                    {/* Conditionally render the heart icon based on whether it's a favorite or not */}
                    {favoriteProperties.some(favProperty => favProperty.id === property.id) ? (
                      <img src="https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678087-heart-64.png"
                        className="heart-icon liked" 
                        alt="Heart Icon" 
                      />
                    ) : (
                      <img
                        src="https://cdn4.iconfinder.com/data/icons/basic-ui-2-line/32/heart-love-like-likes-loved-favorite-64.png" 
                        className="heart-icon" 
                        alt="Heart Icon" 
                      />
                    )}
                  </button>
                  {/* Use the Link component to redirect to the PropertyDetails page */}
                  <Link to={`/propertyDetails/${property.id}`}>
                    <button>Details</button>
                  </Link>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Properties;