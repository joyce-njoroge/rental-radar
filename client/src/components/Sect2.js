import React, { useEffect, useState, useRef } from 'react';
import '../CSS/Sect2.css';

function Sect2() {
  const [sect2, setListings] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const translateRef = useRef(0);

  useEffect(() => {
    // Function to fetch the listings using the token
    const fetchListings = async () => {
      const token = localStorage.getItem('access_token');
      if (!token) {
        console.error('Token not found. User is not authenticated.');
        return;
      }

      try {
        const response = await fetch('/newestlistings', {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch listings.');
        }

        const data = await response.json();
        // Duplicate the listings to create an endless loop
        setListings([...data, ...data]);
        console.log(data); // Logging the fetched data to the console
      } catch (error) {
        console.error('Error fetching listings:', error);
      }
    };

    fetchListings();
  }, []);

  useEffect(() => {
    // Start the automatic sliding after 30 seconds
    const interval = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % (sect2.length / 2));
    }, 30000);

    // Clear the interval when the component unmounts
    return () => clearInterval(interval);
  }, [sect2]);

  useEffect(() => {
    // Update the translateX value when currentIndex changes
    translateRef.current = currentIndex * -240; // Increased card width

    // When the currentIndex reaches the last real slide, we smoothly move the slide back to the start
    if (currentIndex === sect2.length / 2 - 1) {
      setTimeout(() => {
        setCurrentIndex(0);
        translateRef.current = 0;
      }, 1000);
    }
  }, [currentIndex, sect2]);

  return (
    <div className="horizontal">
      <div
        className="section2"
        style={{
          transform: `translateX(${translateRef.current}px)`,
          transition: 'transform 1s',
        }}
      >
        {sect2.map((item, index) => (
          <div key={index} className="small-cont">
            <div className="rect">
              <img src={item.media} alt="pic" />
            </div>
            <p className="item-title">{item.title}</p>
        <p className="rent-text">Rent: Kshs{item.rent}</p>
        <p className="size-text">Size: {item.size}</p>
        <p className="address-text">Address: {item.place}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Sect2;