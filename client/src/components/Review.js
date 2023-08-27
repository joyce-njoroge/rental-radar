import React, { useState } from 'react';

function ReviewForm() {
  // Generate random user_id and property_id
  const randomUserId = Math.floor(Math.random() * 1000);
  const randomPropertyId = Math.floor(Math.random() * 1000);

  const [formData, setFormData] = useState({
    full_name: '',
    address: '',
    email: '',
    comment: '',
  });

  const { full_name, address, email, comment } = formData;

  const handleChange = e => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async e => {
    e.preventDefault();

    const data = {
      user_id: randomUserId,       // Use the generated random user_id
      property_id: randomPropertyId, // Use the generated random property_id
      full_name: full_name,
      address: address,
      email: email,
      comment: comment,
      // Include the current date and time in ISO format
      review_date: new Date().toISOString()
    };
    
    try {
      const response = await fetch("/reviews", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const responseData = await response.json();
      alert(responseData.message);

      // Clear the form fields after successful submission
      setFormData({
        full_name: '',
        address: '',
        email: '',
        comment: '',
      });
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="review-form">
      {/* <h2>Leave a Review</h2> */}
      <form onSubmit={handleSubmit}>
        <label htmlFor="full_name">Full Name:</label>
        <input
          type="text"
          id="full_name"
          value={full_name}
          onChange={handleChange}
          name="full_name"
          required
        />
        <br />

        <label htmlFor="address">Address:</label>
        <input
          type="text"
          id="address"
          value={address}
          onChange={handleChange}
          name="address"
          required
        />
        <br />

        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={handleChange}
          name="email"
          required
        />
        <br />

        <label htmlFor="comment">Review:</label>
        <textarea
          id="comment"
          value={comment}
          onChange={handleChange}
          name="comment"
          rows="4"
          cols="50"
          required
        />
        <br />

        <button type="submit">Submit Review</button>
      </form>
    </div>
  );
}

export default ReviewForm;

