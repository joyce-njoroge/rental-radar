import React from 'react'
import Sect from './Sect'
import Sect1 from './Sect1'
import Sect2 from './Sect2'
import Sect3 from './Sect3'

import "../CSS/Homepage.css"

function Homepage() {
  return (
    <div>
    <Sect />
  
    <br />
   
      <h2 className="section-title">Discover the Best Listings in the Cities</h2>
      <p className="section-description">Find the perfect rental home and commercial space to suit your needs. Explore all available listings now.</p>
   
    <br />
  
    <Sect1 />
    <br />
  
      <h2 className="section-title">Newest Listings</h2>
      <p className="section-description">See the most up-to-date listings</p>
    
  
    <Sect2 />
    <br />
   
      <h2 className="section-title">Featured Listings</h2>
      <p className="section-description">We have a variety of rental listings for renting in your area.</p>
  
    <Sect3 />
  </div>
  
  )
}

export default Homepage