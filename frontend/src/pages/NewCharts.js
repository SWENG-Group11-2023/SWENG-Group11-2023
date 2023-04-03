import React, { useState } from 'react';
import {data} from './DataFetching';
import { PieChart, Pie, BarChart, Bar, LineChart, Line, Tooltip, CartesianGrid, XAxis, YAxis, Legend } from 'recharts';

function Chart() {
  const [Userdata, setData] = useState([
    { name: 'January', uv: 10 },
    { name: 'February', uv: 20 },
    { name: 'March', uv: 30 },
    { name: 'April', uv: 40 },
  ]);

  const updateData = () => {
    const newData = [
    [{"name": data.data[0].name ,"value": data.data[0].value}]
    ];
    setData(newData);
  };

  return (
    <div>
      <button onClick={updateData}>Update Data</button>
      
      {
       <BarChart
       width={400}
       height={300}
       data={data.data}
       margin={{
         top: 5,
         right: 30,
         left: 70,
         bottom: 5,
       }}
     >
       <CartesianGrid strokeDasharray="3 3" />
       <XAxis dataKey="name" />
       <YAxis />
       <Tooltip />
       <Legend />
       <Bar dataKey="value" fill="#8884d8" />
     
   </BarChart>
    
      /* <LineChart width={400} height={400} data={data}>
        <XAxis dataKey="name" />
        <YAxis />
        <CartesianGrid stroke="#ccc" />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
      </LineChart> */}
    </div>
  );
}

export default Chart;