import React from 'react';
import axios from 'axios';
import { useState, useEffect } from "react";    
import { FaSearch } from 'react-icons/fa';



var data = ({});


function DataFetching() {
    const [dataPionts, setDataPionts ] = useState({})
    const [query, setQuery ] = useState('')
    const [updatedQuery, setUpdatedQuery ] = useState('')

    useEffect(() => { 
            const getData = async () => {
                // turns the user input into a form that the backend can read
               // data = backendReadableText(data);

                data = await axios.get(`http://localhost/query/${updatedQuery}`)
                setDataPionts(data)
                console.log(data) 
            };
            getData();
        }, [updatedQuery])

        const handleKeyDown = (e) => {
            if(e.key === 'Enter'){
                console.log('do validate')
                setUpdatedQuery(query);
            }
        };
        const handleChange = (e) =>{
            setQuery(e.target.value)
        }

    return (
        <div>
           <FaSearch />
            <input 
                placeholder='search...'
                type="text"
                value={query}
                onChange = {handleChange}    
               onKeyDown ={handleKeyDown}   
            />
           {dataPionts.data ? <h2>{dataPionts.data}</h2> : null}  
      
        </div>

    )
}
function backendReadableText(userInput){
    let charArray = userInput;
    charArray = String(charArray);
    let array = charArray.split("");
    // I can change what the replacement character is depending on what the backend team has.
    array = charArray.replaceAll(' ', "+");
    return array.toString();
}
export { DataFetching };
