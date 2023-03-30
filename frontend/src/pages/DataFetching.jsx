import React from 'react';
import axios from 'axios';
import { useState, useEffect } from "react";
import { FaSearch } from 'react-icons/fa';



var data = [{ "name": "0.0,14.257", "value": 200.0 }, { "name": "14.257,28.514", "value": 163.0 },
{ "name": "28.514,42.771", "value": 168.0 }, { "name": "42.771,57.029", "value": 238.0 },
{ "name": "57.029,71.286", "value": 261.0 }, { "name": "71.286,85.543", "value": 308.0 },
{ "name": "85.543,99.8", "value": 277.0 }];
//var data =  axios.get('http://localhost/query/give%20me%20a%20list%20of%20patients%20total%20cholesterol')



function DataFetching() {
    const [dataPionts, setDataPionts] = useState({})
    const [query, setQuery] = useState('')
    const [updatedQuery, setUpdatedQuery] = useState('')

    useEffect(() => {
        const getData = async () => {
            data = await axios.get(`http://localhost/query/${updatedQuery}`)
            setDataPionts(data.data)
            console.log(data.data)
        };
        getData();
    }, [updatedQuery])

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            console.log('do validate')
            setUpdatedQuery(query);
         
        }
    };
    const handleChange = (e) => {
        setQuery(e.target.value)
    }

    return (
        <div>
            <FaSearch />
            <input
                placeholder='search...'
                type="text"
                value={query}
                onChange={handleChange}
                onKeyDown={handleKeyDown}
            />
            
        </div>

    )
}
export { DataFetching, data };
