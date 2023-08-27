import React from 'react';
import '../CSS/Signup.css'


function Signup() {

  
  return (
    <div className="cont">
      <div className="text-center">
      <h1 className="h3 mb-3 font-weight-normal">
        Join our  RentalRader
      </h1>
      </div>
      
      <br />
      <div className="card-deck">
        <div className="card text-center renter-card clickable-card">
          <div className="card-body">
            <span className="selection-indicator"></span>
            <h5 className="card-title">
              I'm Tenant, looking for property to rent
            </h5>
            <a href="/Tenantsignup" className="btn btn-success sign-up-button">
              Join as a Tenant
            </a>
          </div>
        </div>
        {/* <div className="card text-center owner-card clickable-card">
          <div className="card-body">
            <span className="selection-indicator"></span>
            <h5 className="card-title">
              I'm a Property Owner, Submitting Property/Properties To Rent
            </h5>
            <a
              href="/Ownersignup"
              className="btn btn-success sign-up-button"
            >
              Apply as a Property Owner
            </a>
          </div>
        </div> */}
      </div>
      <br />
      <div className="text-center">
        <p>
          Already have an account? <a href="/login">Sign In</a>
        </p>
      </div>
    </div>
  );
}

export default Signup;
