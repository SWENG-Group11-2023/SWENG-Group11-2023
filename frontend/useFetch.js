import axios from 'axios';
import { useEffect, useState } from "react";

function useFetch(url) {
    const [data, setData] = useState(null);
    const [loading, setloading] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        setloading(true);
        axios.get(url).then((response) => {
            setData(response.data);
        }).catch((err) => {
            setError(err);
        }).finally(() => {
            setloading(false);
        });
    }, [url]);  

    return {data, loading, error};
}

export default useFetch