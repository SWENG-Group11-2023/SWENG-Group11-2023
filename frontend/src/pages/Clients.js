import React from 'react'
import img1 from './images/ibm-research-logo.jpg'

function Clients() {
  return (
    <div style={{textAlign: "center"}} > 
      <h1>Clients page</h1>
      <p> IBM Research </p>
      <br></br>
      <p>
      Our client, IBM Research is constantly working on improving various 
      aspects of computing such as AI and quantum computing. 
      IBM Research is currently working on ways to solve important healthcare problems 
      and their first objective is to decrease the time it takes to discover new drugs 
      and treatment approaches. Analysing the results of clinical trials is one way 
      to tackle this.
      </p>
      <p>meet our team.</p>

      <div classeName = "images">
            <img src={img1} alt=''/>
            <img src={img1} alt=''/>
            <img src={img1} alt=''/>
      </div>
    </div>
  )
}

export default Clients