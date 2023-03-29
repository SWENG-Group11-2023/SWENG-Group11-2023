import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { data} from './DataFetching';

function Chart() {
  const [Userdata, setData] = useState([
    { name: 'January', uv: 10 },
    { name: 'February', uv: 20 },
    { name: 'March', uv: 30 },
    { name: 'April', uv: 40 },
  ]);

  const updateData = () => {
    const newData = [
      data.data[0],
    ];
    setData(newData);
  };

  return (
    <div>
      <button onClick={updateData}>Update Data</button>
      <LineChart width={400} height={400} data={Userdata}>
        <XAxis dataKey="name" />
        <YAxis />
        <CartesianGrid stroke="#ccc" />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
      </LineChart>
    </div>
  );
}

export default Chart;