import React from 'react';
import axios from 'axios';
import { useState, useEffect } from "react";    
import { FaSearch } from 'react-icons/fa';



var data = [{name: "isobel", value:10}, {name:"Cillian", value: 20}];



function DataFetching() {
    const [dataPionts, setDataPionts ] = useState({})
    const [query, setQuery ] = useState('')
    const [updatedQuery, setUpdatedQuery ] = useState('')

    useEffect(() => { 
            const getData = async () => {

                data = await axios.get(`http://localhost/query/${updatedQuery}`)
                setDataPionts(data.data)
                console.log(data.data) 
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
        </div>

    )
}
export { DataFetching, data };
