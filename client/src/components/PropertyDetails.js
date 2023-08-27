// PropertyDetails.js
import React, { useEffect, useState } from 'react';
import '../CSS/PropertyDetails.css'; // Import your custom CSS file
import { useParams } from 'react-router-dom';
import axios from 'axios';
import Review from './Review';
import PropertyInquiryForm from './PropertyInquiryForm';
import Mpesa from './Mpesa';


function PropertyDetails({ user_id, property_id, match }) {
  const [propertyDetails, setPropertyDetails] = useState({}); // State to store fetched property details


  const { id: propertyId } = useParams(); // Extracting the listing ID from the URL params

  useEffect(() => {
    // Fetching listings details from the server using property ID
    fetch(`/properties/${propertyId}`)
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setPropertyDetails(data);
      })
      .catch(error => {
        console.error('Error fetching property details:', error);
      });
  }, [propertyId]);

  // Function to handle the image carousel
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  const handleNextImage = () => {
    // Implementing logic to move to the next image in the carousel
    const imageUrls = propertyDetails.images.split(',').map((url) => url.trim());
    const nextIndex = (currentImageIndex + 1) % imageUrls.length;
    setCurrentImageIndex(nextIndex);
  };
  
  const handlePreviousImage = () => {
    // Implementing logic to move to the previous image in the carousel
    const imageUrls = propertyDetails.images.split(',').map((url) => url.trim());
    const prevIndex = (currentImageIndex - 1 + imageUrls.length) % imageUrls.length;
    setCurrentImageIndex(prevIndex);
  };
  
  const renderImageCarousel = () => {
    if (propertyDetails.images && typeof propertyDetails.images === 'string') {
      const imageUrls = propertyDetails.images.split(',').map((url) => url.trim());
      if (imageUrls.length > 0) {
        // Slice the array to show up to three images at a time
        const visibleImages = imageUrls.slice(currentImageIndex, currentImageIndex + 3);
        return (
          <div className="image-carousel">
            <button className="prev-button" onClick={handlePreviousImage}>&lt;</button>
            <div className="image-container">
              {visibleImages.map((imageUrl, index) => (
                <img
                  key={index}
                  src={imageUrl}
                  alt={`Listing ${currentImageIndex + index + 1}`}
                />
              ))}
            </div>
            <button className="next-button" onClick={handleNextImage}>&gt;</button>
          </div>
        );
      }
    }
  };

  
  return (
      <div className="property-details-container">
        {/* Section 1: Images */}
        {renderImageCarousel()}
    
        {/* Section 2: Overview, Description, Property Owner, and Inquire Form */}
        <div className="sections-container">
          {/* Left Section: Overview and Description */}
          <div className="left-section">
            <div className="overview">
              <h2>Overview</h2>
              <p>Property Title: {propertyDetails.property_title}</p>
              <p>Property Type: {propertyDetails.property_type}</p>
              <p>Rent: Kshs {propertyDetails.property_rent}</p>
              <p>Bedrooms: {propertyDetails.bedrooms}</p>
              <p>Bathrooms: {propertyDetails.bathrooms}</p>
              <p>Address: {propertyDetails.address}</p>
            </div>
    
            <div className="description">
              <h2>Description</h2>
              <p>{propertyDetails.description}</p>
            </div>
          </div>
    
          {/* Right Section: Property Owner and Inquire Form */}
          <div className="right-section1">
            {/* Property Owner Contact Information */}
            <div className="property-owner">
              <h2>Property Owner</h2>
              <img src={propertyDetails.property_owner_photo} alt="pic" />
              <p>Name: {propertyDetails.property_owner_name}</p>
              <p>Contact Phone: {propertyDetails.contact_phone}</p>
              <p>Contact Email: {propertyDetails.contact_email}</p>
              <p>Contact Whatsapp: {propertyDetails.contact_whatsapp}</p>
              <p>Preferred Contact Method: {propertyDetails.preferred_contact_method}</p>
            </div>
    
               {/* Inquire About This Property Form */}
            <div className="inquire-form">
              <PropertyInquiryForm property_id={property_id} />
            </div>
           </div>
          </div>
    
      {/* Section 3: Overview, Description, and Property Owner */}
      <div className="sections-container">
        {/* Left Section: Address, Property Details, and House Video Tour */}
        <div className="left-section">
          {/* Section 5: Address */}
          <div className="address">
            <h2>Address</h2>
            <p>Address: {propertyDetails.address}</p>
            <p>City: {propertyDetails.city_town}</p>
            <p>Neighbourhood: {propertyDetails.neighborhood_area}</p>
            <p>Country: {propertyDetails.country}</p>
            <a
              href={propertyDetails.googleMapsLink}
              target="_blank"
              rel="noopener noreferrer"
            >
              Open on Google Maps
            </a>
          </div>

          {/* Section 6: Property Details */}
          <div className="property-details">
            <h2>Property Details</h2>
            <p>Property Category: {propertyDetails.property_category}</p>
            <p>Furnished: {propertyDetails.furnished}</p>
            <p>Property Rent: {propertyDetails.property_rent}</p>
            <p>Bedrooms: {propertyDetails.bedrooms}</p>
            <p>Bathrooms: {propertyDetails.bathrooms}</p>
            <p>Amenities: {propertyDetails.amenities}</p>
          </div>

          {/* Section 7: House Video Tour */}
          <div className="house-video-tour">
            <h2>House Video Tour</h2>
            <video controls>
              <source src={propertyDetails.house_tour_video} type="video/mp4" />
              Your browser does not support the video tag.
            </video>
          </div>
        </div>

          {/* Right Section: Review */}
          <div className="right-section2">
            <div className="section-title">Leave a Review</div>
            <div className="review-form">
              <Review user_id={user_id} property_id={property_id} />
            </div>

            {/* Mpesa Section */}
            <div className="mpesa-section">
              <Mpesa />
            </div>
          </div>
        </div>
      </div>
  );
  }

  export default PropertyDetails;