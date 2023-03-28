import React from 'react';
import axios from 'axios';
import { useState, useEffect } from "react";
import { FaSearch } from 'react-icons/fa';



var data = [{ "name": "60.0,65.714", "value": 1820.0 }, { "name": "65.714,71.429", "value": 1942.0 }, { "name": "71.429,77.143", "value": 1894.0 }, { "name": "77.143,82.857", "value": 1510.0 }, { "name": "82.857,88.571", "value": 1904.0 }, { "name": "88.571,94.286", "value": 1787.0 }, { "name": "94.286,100.0", "value": 1695.0 }];



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
