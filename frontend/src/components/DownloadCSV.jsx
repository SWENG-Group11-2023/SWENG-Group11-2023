import React, { useState } from "react";
import axios from "axios";
import { DataFetching } from "../pages/DataFetching";

function DownloadButton() {
    const [CSVData, setCSVData] = useState({});

    const fetchData = async () => {
        const data = await axios.get(`http://localhost/download/${DataFetching.updatedQuery}`)
        setCSVData(data.data);
        console.log(data.data);
    };
    
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
    
    return (
        <div>
            <button onClick={() => { fetchData(); }}> Fetch data </button>
            <button onClick={() => { downloadCSV(); }}> Download data </button>
        </div>
    );
}

export default DownloadButton;