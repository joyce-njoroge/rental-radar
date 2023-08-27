import React, { useEffect, useState } from 'react';
import '../CSS/Listings.css'; // Import your custom CSS file
import { Link } from 'react-router-dom';

function Listings() {
    const [listings, setListings] = useState([]);
    const [favoriteListings, setFavoriteListings] = useState([]);
    
    
    useEffect(() => {
        fetch('/listings')
        .then(res => res.json())
        .then(data => {
            console.log(data);
            setListings(data);
        });
    }, []);
    
    const handleLikeListing = async (listing) => {
        if (favoriteListings.some(favListing => favListing.id === listing.id)) {
        // Unlike the listing and remove it from favorites
        setFavoriteListings(prevFavorites => prevFavorites.filter(favListing => favListing.id !== listing.id));
        try {
            await fetch(`/fav/${listing.id}`, {
            method: 'DELETE',
            });
        } catch (error) {
            console.error('Error removing listing from favorites:', error);
            // Handle error if needed
        }
        } else {
        // Like the listing and add it to favorites
        setFavoriteListings(prevFavorites => [...prevFavorites, listing]);
        try {
            await fetch('/fav', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id: listing.id }), // Send the listing ID in the request body
            });
        } catch (error) {
            console.error('Error adding listing to favorites:', error);
            // Handle error if needed
        }
        }
    };
      
  return (
    <div className="custom-listings-container">
      <div className="custom-row">
        {listings.map(listing => (
          <div key={listing.id} className="custom-col-md-6 custom-col-lg-4 custom-mb-4">
            <div className="custom-card custom-listing-card">
              <div className="card-buttons">
              </div>
              <div className="image-container">
                <img src={listing.media} className="custom-card-img-top custom-listing-img" alt="Listing" />
              </div>
              <div className="custom-card-body">
                <h5 className="custom-card-title">{listing.title}</h5>
                <p className="custom-card-text">{listing.description}</p>
                <p className="custom-card-text">Rent: {listing.rent}</p>
                <p className="custom-card-text">Location: {listing.place}</p>
                <p className="custom-card-text">Utilities: {listing.utilities}  </p>
                <div className="card-buttons">
                  <button onClick={() => handleLikeListing(listing)}>
                    {/* Conditionally render the heart icon based on whether it's a favorite or not */}
                    {favoriteListings.some(favListing => favListing.id === listing.id) ? (
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
                  {/* Use the Link component to redirect to the ListingDetails page */}
                  <Link to={`/ListingDetails/${listing.id}`}>
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

export default Listings