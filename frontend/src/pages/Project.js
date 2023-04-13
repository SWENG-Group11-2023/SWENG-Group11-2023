import React from 'react'
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import JS_Logo from './images/JS_logo.png'
import React_Logo from './images/react_logo.png'
import Python_Logo from './images/python_logo.png'
import sqlite_Logo from './images/sqlite_logo.png'

function Project() {
  return (
    <Container fluid>
      <div style={{textAlign: "center", padding:"60px"}}> 
        <h1> Find out more about our project!</h1>
        <p> 
          This web application was built using JavaScript, the React library, Python, SQLite and
          The Natural Language Toolkit (NLTK).
        </p>
      </div>
      <Row>
        <Col md={{offset:1}}>
          <img
          alt="JavaScript logo"
          src={JS_Logo}
          style={ {height: "155px", width: "240px"}}
          />
        </Col>
        <Col>
          <img
          alt="React logo"
          src={React_Logo}
          style={{height: "135px", width: "150px"}}
          />
        </Col>
        <Col>
          <img
          alt="Python logo"
          src={Python_Logo}
          style={{height: "150px", width: "150px"}}
          />
        </Col>
        <Col>
          <img
          alt="SQLite logo"
          src={sqlite_Logo}
          style={{height: "140px", width: "140px"}}
          />
        </Col>
      </Row>
      <div style={{textAlign: "center", padding:"20px"}}> 
        <p> 
          Our team consisted of students from <span class="fw-bold"> Integrated Computer Science </span> 
          and  <span class="fw-bold"> Computer Science and Business </span>. We had three third year students and six second years. The second years
          were broken up into two teams of three, a <span class="fw-bold"> frontend </span> and a <span class="fw-bold"> backend </span> team. The third years
          managed the project and helped out each team.
        </p>
      </div>
      <div style={{textAlign: "center", padding:"20px"}}> 
        <h2>Project Specifications</h2>
        <p> • Develop a <span class="fw-bold"> dashboard </span> that <span class="fw-bold"> summarises population characteristics </span> through <span class="fw-bold"> charts </span> </p>
        <p> • Users <span class="fw-bold"> interact </span> with the app through <span class="fw-bold"> Natural Language </span> </p>
        <p> • Responses are provided in <span class="fw-bold"> real-time </span> and must be available for <span class="fw-bold"> download </span> </p>
      </div>
    </Container>
  )
}

export default Project