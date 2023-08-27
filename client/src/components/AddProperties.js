import React, { useState } from 'react';
import "../CSS/Addpro.css"
import axios from 'axios'; // Import Axios for making API requests

function AddProperty() {
  const [formData, setFormData] = useState({
    // Initialize the form data state
    property_title: '',
    property_type: '',
    property_category: '',
    property_rent: '',
    bedrooms: '',
    bathrooms: '',
    amenities: '',
    square_footage: '',
    main_image: '',
    images: [],
    house_tour_video: '',
    property_documents: [],
    description: '',
    location_details: '',
    country: '',
    city_town: '',
    neighborhood_area: '',
    address: '',
    property_owner_name: '',
    property_owner_photo: '',
    contact_phone: '',
    contact_whatsapp: '',
    contact_email: '',
    facebook: '',
    twitter: '',
    instagram: '',
    linkedin: '',
    other_social_media: '',
    preferred_contact_method: '',
    additional_details: '',
  });

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      // Send a POST request to the API endpoint
      const response = await axios.post('/properties', formData);
      console.log('Property added:', response.data);
      // Clear the form after successful submission
      setFormData({
        property_title: '',
        property_type: '',
        property_category: '',
        property_rent: '',
        bedrooms: '',
        bathrooms: '',
        amenities: '',
        square_footage: '',
        main_image: '',
        images: [],
        house_tour_video: '',
        property_documents: [],
        description: '',
        location_details: '',
        country: '',
        city_town: '',
        neighborhood_area: '',
        address: '',
        property_owner_name: '',
        property_owner_photo: '',
        contact_phone: '',
        contact_whatsapp: '',
        contact_email: '',
        facebook: '',
        twitter: '',
        instagram: '',
        linkedin: '',
        other_social_media: '',
        preferred_contact_method: '',
        additional_details: '',
      });
    } catch (error) {
      console.error('Error adding property:', error);
    }
  };

  const handleChange = e => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  return (
    <div className="add-property-container">
      <h2>Add Property</h2>
      <form onSubmit={handleSubmit} className="property-form">
    <label htmlFor="propertyTitle">Property Title:</label>
    <input
      type="text"
      id="property_title"
      name="property_title"
      value={formData.property_title}
      onChange={handleChange}
      required
    />

    <label htmlFor="property_type">Property Type:</label>
    <select
      id="property_type"
      name="property_type"
      value={formData.property_type}
      onChange={handleChange}
      required
    >
      <option value="">Select Property Type</option>
      <option value="House">House</option>
      <option value="Apartment">Apartment</option>   
    </select>
    {/* Section 3: Property Category and Rent */}
  <div className="form-section"> 
    <label htmlFor="property_category">Property Category:</label>
    <select
      id="property_category"
      name="property_category"
      value={formData.property_category}
      onChange={handleChange}
      required
    >
      <option value="">Select Property Category</option>
      <option value="Residential">Residential</option>
      <option value="Commercial">Commercial</option>
      {/* Add more property categories */}
    </select>

    <label htmlFor="property_rent">Property Rent:</label>
    <input
      type="text"
      id="property_rent"
      name="property_rent"
      value={formData.property_rent}
      onChange={handleChange}
      required
    />
  </div>

  {/* Section 4: Bedrooms and Bathrooms */}
  <div className="form-section">
    <h3>Bedrooms and Bathrooms</h3>
    <label htmlFor="bedrooms">Bedrooms:</label>
    <input
      type="number"
      id="bedrooms"
      name="bedrooms"
      value={formData.bedrooms}
      onChange={handleChange}
      required
    />

    <label htmlFor="bathrooms">Bathrooms:</label>
    <input
      type="number"
      id="bathrooms"
      name="bathrooms"
      value={formData.bathrooms}
      onChange={handleChange}
      required
    />
  </div>

  {/* Section 5: Amenities and Square Footage */}
  <div className="form-section">
    <h3>Amenities and Square Footage</h3>
    <label htmlFor="amenities">Amenities (comma-separated):</label>
    <input
      type="text"
      id="amenities"
      name="amenities"
      value={formData.amenities}
      onChange={handleChange}
    />

    <label htmlFor="square_footage">Square Footage:</label>
    <input
      type="text"
      id="square_footage"
      name="square_footage"
      value={formData.square_footage}
      onChange={handleChange}
    />
  </div>

  {/* Section 6: Main Image and Additional Images */}
  <div className="form-section">
    <h3>Main Image and Additional Images</h3>
    <label htmlFor="main_image">Main Image URL:</label>
    <input
      type="text"
      id="main_image"
      name="main_image"
      value={formData.main_image}
      onChange={handleChange}
      required
    />

    <label htmlFor="images">Additional Images URLs (comma-separated):</label>
    <input
      type="text"
      id="images"
      name="images"
      value={formData.images}
      onChange={handleChange}
      required
    />
  </div>
    
     {/* Section 7: House Tour Video and Property Documents */}
  <div className="form-section">
    <h3>House Tour Video and Property Documents</h3>
    <label htmlFor="house_tour_video">House Tour Video URL:</label>
    <input
      type="text"
      id="house_tour_video"
      name="house_tour_video"
      value={formData.house_tour_video}
      onChange={handleChange}
    />

    <label htmlFor="property_documents">Property Documents URLs (comma-separated):</label>
    <input
      type="text"
      id="property_documents"
      name="property_documents"
      value={formData.property_documents}
      onChange={handleChange}
    />
  </div>

  {/* Section 8: Description and Location Details */}
  <div className="form-section">
    <h3>Description and Location Details</h3>
    <label htmlFor="description">Description:</label>
    <textarea
      id="description"
      name="description"
      value={formData.description}
      onChange={handleChange}
    />

    <label htmlFor="location_details">Location Details:</label>
    <textarea
      id="location_details"
      name="location_details"
      value={formData.location_details}
      onChange={handleChange}
    />
  </div>

  {/* Section 9: Address and Contact Information */}
  <div className="form-section">
    <h3>Address and Contact Information</h3>
    <label htmlFor="country">Country:</label>
    <input
      type="text"
      id="country"
      name="country"
      value={formData.country}
      onChange={handleChange}
    />

    <label htmlFor="city_town">City/Town:</label>
    <input
      type="text"
      id="city_town"
      name="city_town"
      value={formData.city_town}
      onChange={handleChange}
    />

    <label htmlFor="neighborhood_area">Neighborhood/Area:</label>
    <input
      type="text"
      id="neighborhood_area"
      name="neighborhood_area"
      value={formData.neighborhood_area}
      onChange={handleChange}
    />

    <label htmlFor="address">Address:</label>
    <input
      type="text"
      id="address"
      name="address"
      value={formData.address}
      onChange={handleChange}
    />
  </div>

  {/* Section 10: Property Owner and Contact Details */}
  <div className="form-section">
    <h3>Property Owner</h3>
    <label htmlFor="property_owner_name"> Name:</label>
    <input
      type="text"
      id="property_owner_name"
      name="property_owner_name"
      value={formData.property_owner_name}
      onChange={handleChange}
      required
    />

    <label htmlFor="property_owner_photo">Photo:</label>
    <input
      type="text"
      id="property_owner_photo"
      name="property_owner_photo"
      value={formData.property_owner_photo}
      onChange={handleChange}
    />

    <label htmlFor="contact_phone">Contact Phone:</label>
    <input
      type="text"
      id="contact_phone"
      name="contact_phone"
      value={formData.contact_phone}
      onChange={handleChange}
      required
    />

    <label htmlFor="contact_whatsapp">Contact WhatsApp:</label>
    <input
      type="text"
      id="contact_whatsapp"
      name="contact_whatsapp"
      value={formData.contact_whatsapp}
      onChange={handleChange}
    />

    <label htmlFor="contact_email">Contact Email:</label>
    <input
      type="email"
      id="contact_email"
      name="contact_email"
      value={formData.contact_email}
      onChange={handleChange}
      required
    />

    {/* Add more fields for property owner and contact details */}
  </div>

  {/* Section 5: Social Media */}
  <div className="form-section">
    <h3>Social Media</h3>
    <label htmlFor="facebook">Facebook:</label>
    <input
      type="text"
      id="facebook"
      name="facebook"
      value={formData.facebook}
      onChange={handleChange}
    />

    <label htmlFor="twitter">Twitter:</label>
    <input
      type="text"
      id="twitter"
      name="twitter"
      value={formData.twitter}
      onChange={handleChange}
    />

    <label htmlFor="instagram">Instagram:</label>
    <input
      type="text"
      id="instagram"
      name="instagram"
      value={formData.instagram}
      onChange={handleChange}
    />

    <label htmlFor="linkedin">LinkedIn:</label>
    <input
      type="text"
      id="linkedin"
      name="linkedin"
      value={formData.linkedin}
      onChange={handleChange}
    />

    <label htmlFor="other_social_media">Other Social Media:</label>
    <input
      type="text"
      id="other_social_media"
      name="other_social_media"
      value={formData.other_social_media}
      onChange={handleChange}
    />
  </div>
  {/* Section 6: Contact Preferences */}
  <div className="form-section">
    <label htmlFor=" preferred_contact_method">Preferred Contact Method:</label>
    <select
      id=" preferred_contact_method"
      name=" preferred_contact_method"
      value={formData.preferred_contact_method}
      onChange={handleChange}
    >
      <option value="">Select Contact Method</option>
      <option value="phone">Phone</option>
      <option value="whatsapp">WhatsApp</option>
      <option value="email">Email</option>
    </select>
  </div>

  {/* Section 7: Additional Details */}
  <div className="form-section">
    <label htmlFor=" additional_details">Additional Details:</label>
    <textarea
      id=" additional_details"
      name=" additional_details"
      value={formData.additional_details}
      onChange={handleChange}
    />
  </div>
        <button type="submit">Add Property</button>
      </form>
    </div>
  );
}

export default AddProperty;
