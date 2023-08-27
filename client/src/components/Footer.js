import React from 'react';
import '../CSS/Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <h3>Get to Know Us</h3>
          <ul>
            <li><a href="#about">About Us</a></li>
            <li><a href="#privacy">Privacy Policy</a></li>
            <li><a href="#terms">Terms & Conditions</a></li>
          </ul>
        </div>
        <div className="footer-section">
          <h3>Quick Links</h3>
          <ul>
            <li><a href="#faq">FAQ</a></li>
            <li><a href="#contact">Contact Us</a></li>
            <li><a href="#sitemap">Sitemap</a></li>
            {/* <li><a href="#blogs">Blogs</a></li> */}
          </ul>
        </div>
        <div className="footer-section">
          <h3>Contacts</h3>
          <p>Email: info@Rental-rader.com</p>
          <p>Phone: 0768182022</p>
          <p>Address: 235743, Muthaiga, Nairobi</p>
        </div>
        <div className="footer-section">
          <h3>Follow Us</h3>
          <div className="social-media">
              <a href="https://www.facebook.com"><i className="fab fa-facebook"></i></a>
              <a href="https://www.twitter.com"><i className="fab fa-twitter"></i></a>
              <a href="https://www.instagram.com"><i className="fab fa-instagram"></i></a>
              <a href="https://www.pinterest.com"><i className="fab fa-pinterest"></i></a>
              <a href="https://www.tiktok.com"><i className="fab fa-tiktok"></i></a>
          </div>
        </div>
      </div>
      <p>&copy; 2023 RentalRader. All rights reserved.</p>
    </footer>
  );
}

export default Footer;