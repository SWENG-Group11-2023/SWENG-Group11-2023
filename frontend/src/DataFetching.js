import React from 'react';
import axios from 'axios';
import {  useState , useEffect} from "react";


var data = ({})
var dataPionts = ({})
var id =({})
function DataFetching() {
  const [dataPionts, setDataPionts] = useState({})
    const [id, setId] = useState({})


    useEffect(()=>{
      const getData = async () => {
         data = await axios.get(`http://127.0.0.1:8000/patient/${id}`)
        setDataPionts(data)
      };
      getData();
    },[id] )

  console.log("data: ",dataPionts)

  return (
    <div>
    <input 
    type = "text" 
    value = {id} 
    onChange={e => setId(e.target.value)}
    />
      {dataPionts.data ? <h2>patient: {dataPionts.data}</h2> : null}
    </div>
  )
}
export  {DataFetching, dataPionts, data, id};
