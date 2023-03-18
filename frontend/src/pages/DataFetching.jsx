import React from 'react';
import axios from 'axios';
import { useState, useEffect } from "react";


var data = ({});


function DataFetching() {
    const [dataPionts, setDataPionts] = useState({})
    const [id, setId] = useState({})

    useEffect(() => {
            const getData = async () => {
                // turns the user input into a form that the backend can read i.e. adding
                data = backendReadableText(data);

                data = await axios.get(`http://127.0.0.1:8000/patient/${id}`)
                setDataPionts(data)
            };
            getData();
        }, [id])

        console.log("data: ", dataPionts)
        console.log(id);
    
    


    return (
        <div>
            <input
                type="text"
                value={id}
                onChange={e => setId(e.target.value)}
                
            />

            <h3>Patient ID: </h3>
            {dataPionts.data ? <h2>{dataPionts.data}</h2> : null}
        </div>

    )
}
function backendReadableText(userInput){
    let charArray = userInput;
    charArray = String(charArray);
    let array = charArray.split("");
    // I can change what the replacement character is depending on what the backend team has.
    array = charArray.replaceAll(' ', "%");
    return array;
}
export { DataFetching };
