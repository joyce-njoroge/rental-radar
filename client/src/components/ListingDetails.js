import React, { useEffect, useState } from 'react';
import '../CSS/ListingDetails.css'; // Import your custom CSS file
import { useParams } from 'react-router-dom';
import Mpesa from './Mpesa';

function ListingDetails({ match }) {
  const [listingDetails, setListingDetails] = useState({}); // State to store fetched listing details
  const [formData, setFormData] = useState({
    email: '',
    address: '',
    rating: '',
    review: '',
  });

  const [similarListings, setSimilarListings] = useState([]); // State to store fetched similar listings
  const listingId =  useParams().id; // Extracting the listing ID from the URL params

  useEffect(() => {
    // Fetching listings details from the server using listing ID
    fetch(`/listings/${listingId}`)
      .then(res => res.json())
      .then(data => {
        setListingDetails(data);
      })
      .catch(error => {
        console.error('Error fetching listing details:', error);
      });

    fetch(`/similarListings/${listingId}`) 
      .then(res => res.json())
      .then(data => {
        setSimilarListings(data);
      })
      .catch(error => {
        console.error('Error fetching similar listings:', error);
      });
  }, [listingId]);


  // Function to handle the image carousel
  const handleNextImage = () => {
    // Implementing logic to move to the next image in the carousel
    console.log('Next image');
  };

  const handlePreviousImage = () => {
    // Implementing logic to move to the previous image in the carousel
    console.log('Previous image');
  };

  const handleChange = e => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const response = await fetch('/reviews', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: 1, // Replace with the actual user ID
          listing_id: 123, // Replace with the actual listing ID
          property_id: 456, // Replace with the actual property ID
          comment: formData.review,
          review_date: new Date().toISOString().slice(0, 10), // Today's date in YYYY-MM-DD format
        }),
      });

      if (response.status === 201) {
        console.log('Review submitted successfully');
        setFormData({
          email: '',
          address: '',
          rating: '',
          review: '',
        });
      } else {
        console.error('Failed to submit review');
      }
    } catch (error) {
      console.error('Error submitting review:', error);
    }
  };

  // Function to render the listings features as list items
  const renderListingFeatures = () => {
    if (listingDetails.features && listingDetails.features.length > 0) {
      return listingDetails.features.map((feature, index) => (
        <li key={index}>{feature}</li>
      ));
    } else {
      return <li>No features available</li>;
    }
  };

  return (
    <div className="listing-details-container">
      {/* Section 1: Images */}
      <div className="image-carousel">
        <button onClick={handlePreviousImage}>&lt;</button>
        {/* Replacing the image source with the actual image URLs */}
        {listingDetails.images &&
          listingDetails.images.map((image, index) => (
            <img key={index} src={image} alt={`Listing ${index + 1}`} />
          ))}
        {/* Add more images here */}
        <button onClick={handleNextImage}>&gt;</button>
      </div>

      {/* Section 2: Overview */}
      <div className="overview">
        <h2>{listingDetails.title}</h2>
        <p>{listingDetails.address}</p>
        <p>Rent: {listingDetails.rent}</p>
        <p>Property Type: {listingDetails.listing_type}</p>
        <p>Bedrooms: {listingDetails.bedrooms}</p>
        <p>Bathrooms: {listingDetails.bathrooms}</p>
        <p>Garage: {listingDetails.garage}</p>
        <p>Date Posted: {listingDetails.datePosted}</p>
      </div>

      {/* Section 3: Description */}
      <div className="description">
        <h2>Description</h2>
        <p>{listingDetails.description}</p>
      </div>

      {/* Section 4: Listing Owner */}
      <div className="property-owner">
        <h2>Listing Owner Contact Information</h2>
        <p>{listingDetails.landlord_name}</p>
        <p>{listingDetails.contact_phone}</p>
        <p>{listingDetails.contact_email}</p>
      </div>

      {/* Section 5: Address */}
      <div className="address">
        <h2>Address</h2>
        <p>Address: {listingDetails.address}</p>
        <p>City: {listingDetails.city}</p>
        <p>Neighbourhood: {listingDetails.neighbourhood}</p>
        <p>Country: {listingDetails.country}</p>
        <a href={listingDetails.googleMapsLink} target="_blank" rel="noopener noreferrer">
          Open on Google Maps
        </a>
      </div>

      {/* Section 6: Listing Details */}
      <div className="listing-details">
        <h2>Listing Details</h2>
        <p>Listings ID: {listingDetails.id}</p>
        <p>Bathrooms: {listingDetails.bathrooms}</p>
        <p>Listing Category: {listingDetails.listing_category}</p>
        <p>Garages: {listingDetails.garage}</p>
        <p>Listing Type: {listingDetails.listing_type}</p>
        <p>Posted: {listingDetails.datePosted}</p>
        <h3>Features</h3>
        <ul>{renderListingFeatures()}</ul>
      </div>

      {/* Section 7: House Video Tour */}
      <div className="house-video-tour">
        <h2>Book In Advance</h2>
        <Mpesa/>
      </div>


      {/* Section 8: Review */}
      <div className="review-form">
        <h2>Review</h2>
        <form onSubmit={handleSubmit}>
         <div className="form-group">
          <label>Email:</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
            />
        </div>
        <div className="form-group">
          <label>Address:</label>
          <input
            type="text"
            name="address"
            value={formData.address}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Rating:</label>
          <select
            name="rating"
            value={formData.rating}
            onChange={handleChange}
            required
          >
            <option value="" disabled>Select rating</option>
            <option value="5">5 Stars</option>
            <option value="4">4 Stars</option>
            <option value="3">3 Stars</option>
            <option value="2">2 Stars</option>
            <option value="1">1 Star</option>
          </select>
        </div>
        <div className="form-group">
          <label>Review:</label>
          <textarea
            name="review"
            value={formData.review}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">SUBMIT A REVIEW</button>
      </form>
    </div>

      Section 9: Similar Listings
      <div className="similar-listings">
        <h2>Similar Listings</h2>
        {similarListings.length > 0 ? (
          similarListings.map(listing => (
            <div key={listing.id}>
              <h3>{listing.listing_type}</h3>
              <p>{listing.listing_details}</p>
              <p>Rent: {listing.rent}</p>
              <p>Bedrooms: {listing.bedrooms}</p>
              <p>Bathrooms: {listing.bathrooms}</p>
              <p>Description: {listing.description}</p>
              <p>Landlord Name: {listing.landlord_name}</p>
            </div>
          ))
        ) : (
          <p>No similar listings available</p>
        )}
      </div>
    </div>

  );
};

export default ListingDetails;