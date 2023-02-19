import React from 'react';
import { useEffect, useState } from "react";

function DataFetching() {
    const [dataPionts, setDataPionts] = useState({})
    const [id, setId] = useState([])

  // the api call will only go through if there is text in the searchbar and if enter is pressed
    const HandelKeyDown = event => {
      if (event.key === 'Enter') {
    
    //10339b10-3cd1-4ac3-ac13-ec26728cb592
    const api_url = `http://127.0.0.1:8000/patient/${id}`;
    var array = [];
    
    // function to make only 1 request 
    async function getData(){ 
    const response = await fetch(api_url);
    
    const data = await response.json();
    // this should get all the patient ID'
      for(let i = 0; i< data.length;i++){
    
    // IN THIS CASE WE GET THE "CODE" VALUE WHATEVER THAT IS, either way it is in the 3rd index.
        array.push(data[i][5])
      }    
    }
    getData();
     console.log(array)
  }
}
  return (
    <div>
    <input 
    type = "text" 
    value = {id} 
    onChange={e => setId(e.target.value)}
    onKeyDown= {HandelKeyDown}
    
    />
    </div>
  )
}

export default DataFetching