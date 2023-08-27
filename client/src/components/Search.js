import React, { useState, useEffect } from "react";
import "../CSS/Search.css";

const cities = ["Thika Rd", "Nairobi", "Rongai","Nakuru", "Kiambu", "Kisumu", "Mombasa"];

const Search = () => {
  const [location, setLocation] = useState("");
  const [minRent, setMinRent] = useState(0);
  const [maxRent, setMaxRent] = useState(500000);
  const [selectedCity, setSelectedCity] = useState("");
  const [searchType, setSearchType] = useState("both"); // 'both', 'properties', or 'listings'
  const [propertyResults, setPropertyResults] = useState([]);
  const [listingResults, setListingResults] = useState([]);

  const handleSearch = async (event) => {
    event.preventDefault();
    fetchSearchResults();
  };

  const fetchSearchResults = async () => {
    try {
      const propertyResponse = await fetch(`/properties`);
      const propertyData = await propertyResponse.json();
  
      console.log('Fetched Properties:', propertyData);
  
      const listingResponse = await fetch(`/listings`);
      const listingData = await listingResponse.json();
  
      console.log('Fetched Listings:', listingData);
  
      const filteredProperties = propertyData.filter(
        (property) =>
          property.city_town.includes(selectedCity) &&
          property.property_rent >= minRent &&
          property.property_rent <= maxRent
      );
  
      const filteredListings = listingData.filter((listing) => {
        const meetsPlaceCondition = listing.place.includes(selectedCity);
        const listingRent = parseFloat(listing.rent.replace(/[^0-9.-]+/g, '')); // Extract numeric rent value
        const meetsRentCondition = listingRent >= minRent && listingRent <= maxRent;
      
        console.log(
          'Listing:', listing.id, 'Place:', listing.place, 'Rent:', listing.rent
        );
        console.log(
          'Place Condition:', meetsPlaceCondition, 'Rent Condition:', meetsRentCondition
        );
      
        return meetsPlaceCondition && meetsRentCondition;
      });
      
  
      setPropertyResults(filteredProperties);
      setListingResults(filteredListings);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }
  };
  

  useEffect(() => {
    fetchSearchResults();
  }, [selectedCity, minRent, maxRent, searchType]);

  return (
    <div>
              <div className="search-container">
              <form onSubmit={handleSearch} className="search-form">
              <div className="form-group">
              <label htmlFor="city">Select a City:</label>
              <select
                id="city"
                value={selectedCity}
                onChange={(e) => setSelectedCity(e.target.value)}
                className="select-input"
              >
                <option value="">All Cities</option>
                {cities.map((city) => (
                  <option key={city} value={city}>
                    {city}
                  </option>
                ))}
              </select>
              </div>

              <div className="form-group">
              <label htmlFor="rentRange">Rent Range:</label>
              <input
                type="range"
                id="rentRange"
                min="0"
                max="500000"
                step="1000"
                value={maxRent}
                onChange={(e) => setMaxRent(e.target.value)}
                className="range-input"
              />
              </div>

              <div className="form-group">
              <label htmlFor="minRent">Min Rent:</label>
              <input
                type="number"
                id="minRent"
                name="minRent"
                value={minRent}
                onChange={(e) => setMinRent(e.target.value)}
                className="number-input"
              />
              </div>

              <div className="form-group">
              <label htmlFor="maxRent">Max Rent:</label>
              <input
                type="number"
                id="maxRent"
                name="maxRent"
                value={maxRent}
                onChange={(e) => setMaxRent(e.target.value)}
                className="number-input"
              />
              </div>

              <div className="form-group">
              <label htmlFor="searchType">Search Type:</label>
              <select
                id="searchType"
                value={searchType}
                onChange={(e) => setSearchType(e.target.value)}
                className="select-input"
              >
                <option value="both">Both</option>
                <option value="properties">Properties</option>
                <option value="listings">Listings</option>
              </select>
              </div>

              <button type="submit" className="submit-button">Search</button>
              </form>
              </div>


      <div className="search-results">
        {searchType === "both" || searchType === "properties" ? (
          <div className="horizontal-container">
            {propertyResults.length === 0 ? (
              <p>No property results found.</p>
            ) : (
              propertyResults.map((property) => (
                <a href={`propertyDetails/${property.id}`} key={property.id} className="small-container">
                  <div className="rectangle">
                    <img src={property.main_image} alt={`Property ${property.id}`} />
                  </div>
                  <p>{`Property Rent: ksh${property.property_rent}`}</p>
                  <p>{`Property Rent: ksh${property.address}`}</p>

                </a>
              ))
            )}
          </div>
        ) : null}

        {searchType === "both" || searchType === "listings" ? (
          <div className="horizontal-container">
            {listingResults.length === 0 ? (
              <p>No listing results found.</p>
            ) : (
              listingResults.map((listing) => (
                <a href={`ListingDetails/${listing.id}`} key={listing.id} className="small-container">
                  <div className="rectangle">
                    <img src={listing.media} alt={`Listing ${listing.id}`} />
                  </div>
                  <p>{`Listing Rent: ksh${listing.rent}`}</p>
                  <p>{`Location:${listing.place}`}</p>
                </a>
              ))
            )}
          </div>
        ) : null}
    </div>

    </div>
  );
};

export default Search;
