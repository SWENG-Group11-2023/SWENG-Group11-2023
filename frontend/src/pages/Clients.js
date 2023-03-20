import React from 'react'
import IBM_Logo from './images/ibm_logo.png'

function Clients() {
  return (
    
     <div style={{textAlign: "center", padding:"60px"}}> 
     
      <img
        alt="IBM Research logo"
        src={IBM_Logo}
        style={{height: "70px", width: "600px"}}
      />
      <p>
      <br></br>
      This project was proposed by IBM whose Dublin based Research Lab focuses on improving AI, 
      security, Quantum computing and Cloud computing. The project we are collaborating on is developing 
      a Patient-Centric question answering system with the use of Natural Language Processing. IBM Research 
      is currently working on ways to solve important healthcare problems and their first objective is to decrease 
      the time it takes to discover new drugs and treatment approaches. Analysing the results of clinical trials 
      is one way to tackle this. The aim of this project is to develop a tool to help aid with understanding 
      the characteristics of patients involved in clinical trials in a way that is intuitive and human-accessible.

      </p>
    </div>
  )
}

export default Clients