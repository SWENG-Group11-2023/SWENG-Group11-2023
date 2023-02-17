import React from 'react';
import axios from 'axios';
import { useEffect, useState } from "react";

function DataFetching() {
    const [dataPionts, setDataPionts] = useState({})
    const [id, setId] = useState([])


    const HandelKeyDown = event => {
      if (event.key === 'Enter') {

      }
    }

    useEffect(()=>{
        axios.get(`http://127.0.0.1:8000/${id}`)
        .then(res => {
          setDataPionts(res.data[0])
            console.log(res)    
        })
        .catch(err => {
            console.log(err)
        })
    } )
    
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
