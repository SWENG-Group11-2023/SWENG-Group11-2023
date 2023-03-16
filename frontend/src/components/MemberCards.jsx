import React from 'react';
import {
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBCardText,
  MDBBtn,
  MDBRow,
  MDBCol
} from 'mdb-react-ui-kit';

export default function App() {
  return (
    <MDBRow className='row-cols-1 row-cols-md-3 g-4'>
      <MDBCol>
        <MDBCard>
          <MDBCardBody>
            <MDBCardTitle>Austeja Pakulyte</MDBCardTitle>
            <MDBCardText>
              3rd Year - Intergrated Computer Science
            </MDBCardText>
            <MDBBtn href='https://github.com/pakulyta'>Github</MDBBtn>
          </MDBCardBody>
        </MDBCard>
      </MDBCol>
    </MDBRow>
  );
}