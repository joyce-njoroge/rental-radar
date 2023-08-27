import React, { useState } from 'react';

function PropertyInquiryForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    address: '',
    message: 'Hello, I\'m interested in renting this property.'
  });

  const { name, email, phone, address, message } = formData;

  const generatePropertyId = () => {
    // Generate a random property ID (you can replace this with your own logic)
    return Math.floor(Math.random() * 100000);
  };

  const getCurrentDateTime = () => {
    // Generate the current date and time in the desired format
    const currentDate = new Date();
    return currentDate.toISOString();
  };

  const handleChange = e => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async e => {
    e.preventDefault();

    const data = {
      name: name,
      email: email,
      phone: phone,
      address: address,
      message: message,
      property_id: generatePropertyId(),
      inquiry_date: getCurrentDateTime(),
    };

    try {
      const response = await fetch("/inquiries", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
     <h2>Inquire About This Property</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          value={name}
          onChange={handleChange}
          name="name"
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

        <label htmlFor="phone">Phone:</label>
        <input
          type="tel"
          id="phone"
          value={phone}
          onChange={handleChange}
          name="phone"
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

        <label htmlFor="message">Message:</label>
        <textarea
          id="message"
          value={message}
          onChange={handleChange}
          name="message"
          required
        />
        <br />

        <button type="submit">SEND MESSAGE</button>
      </form>
    </div>
  );
}

export default PropertyInquiryForm;
