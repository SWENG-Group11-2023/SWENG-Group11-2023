import React, { useState } from "react";
import axios from "axios";

function DownloadButton() {
    const [csvData, setCsvdata] = useState([]);
    
    const fetchCSV = async () => {
        try {
            const response = await fetch('/download/this+is+the+query');
            setCsvdata(response.data);
            console.log("DATA RECEIVED: " + csvData);
        } catch (error) {
            console.error(error);
        }
    };
    
    const downloadCSV = () => {
        const csvContents = "data:text/csv;charset=utf-8," + csvData.map(row => row.join(",")).join("\n");
        const encodedURI = encodeURI(csvContents)
        const file = document.createElement("a");
        file.setAttribute("href", encodedURI);
        file.setAttribute("download", "data.csv");
        document.body.appendChild(file);
        file.click();
        document.body.removeChild(file);
    }
    
    return (
        <div>
            <button onClick={() => { fetch();downloadCSV(); }}> Download data </button>
        </div>
    );
}

export default DownloadButton;