import React from 'react';
import axios from 'axios';
import { useState, useEffect } from "react";
import { FaSearch } from 'react-icons/fa';
import { ImFolderDownload } from 'react-icons/im'




var data = [{ "name": "0.0,14.257", "value": 200.0 }, { "name": "14.257,28.514", "value": 163.0 },
{ "name": "28.514,42.771", "value": 168.0 }, { "name": "42.771,57.029", "value": 238.0 },
{ "name": "57.029,71.286", "value": 261.0 }, { "name": "71.286,85.543", "value": 308.0 },
{ "name": "85.543,99.8", "value": 277.0 }];
//var data =  axios.get('http://localhost/query/give%20me%20a%20list%20of%20patients%20total%20cholesterol')


var updatedQuerys;
function DataFetching() {
    var [CSVData, setCSVData] = useState({});
    const [dataPionts, setDataPionts] = useState({})
    const [query, setQuery] = useState('')
    const [updatedQuery, setUpdatedQuery] = useState('')

    useEffect(() => {
        const getData = async () => {
            data = await axios.get(`http://localhost/query/${updatedQuery}`)
            updatedQuerys = updatedQuery
            setDataPionts(data.data)
            console.log(data.data)
            console.log(data.data.values)
            CSVData = await axios.get(`http://localhost/download/${updatedQuery}`)
            setCSVData(CSVData.data);
            console.log(CSVData.data);
        };
        getData();
    }, [updatedQuery])


    const downloadCSV = () => {
        var csvContent = "data:text/csv;charset=utf-8,";
        for (let i = 0; i < CSVData.length; i++) {
            let row = CSVData[i].split(", ");
            csvContent += i < CSVData.length - 1 ? row + "\n" : row;
        }
        const encodedURI = encodeURI(csvContent);
        const file = document.createElement("a");
        file.setAttribute("href", encodedURI);
        file.setAttribute("download", "data.csv");
        document.body.appendChild(file);
        file.click();
        document.body.removeChild(file);
    }

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
            <div>
                <button style={{ width: "50px", height: "50px", color:"light blue"}} onClick={() => { downloadCSV(); }}> <ImFolderDownload size="2em"/> </button>
            </div>
        </div>
    )
}
export { DataFetching, data };
