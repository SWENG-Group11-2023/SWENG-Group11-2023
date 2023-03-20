import React from 'react'
import React_Logo from './images/react_logo.png'

function Project() {
  return (
    <div style={{textAlign: "center", padding:"60px"}}> 
      <h1>Find out more about our project!</h1>
      <br></br>
      <p> 
        This web application was built using JavaScript, the React library, Python, SQLite and
        The Natural Language Toolkit (NLTK).
      </p>
      <img
        alt="React logo"
        src={React_Logo}
        style={{height: "112.5x", width: "150px"}}
      />

      <p>
        <br></br>
        <h3>Project Specifications</h3>
      </p>
    </div>
    
  )
}

export default Project