import React, { useState } from 'react';
import {data} from './DataFetching';
import { PieChart, Pie, BarChart, Bar, LineChart, Line, Tooltip, CartesianGrid, XAxis, YAxis, Legend } from 'recharts';

function Chart() {
  const [Userdata, setData] = useState([
    { "name": "0.0,14.257", "value": 200.0 }, { "name": "14.257,28.514", "value": 163.0 },
{ "name": "28.514,42.771", "value": 168.0 }, { "name": "42.771,57.029", "value": 238.0 },
{ "name": "57.029,71.286", "value": 261.0 }, { "name": "71.286,85.543", "value": 308.0 },
{ "name": "85.543,99.8", "value": 277.0 }
  ]);

  const updateData = () => {
    const newData = 
      data.data.values;
    
    setData(newData);
  };

  return (
    //<div className="graph_orientation">
    <div>
      <button onClick={updateData}>Update Data</button>
      
       <BarChart
       width={400}
       height={300}
       data={Userdata}
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
      
      <PieChart width={350} height={350}>
      <Pie
        margin ={{
         top: 5,
         right: 30,
         left: 70,
         bottom: 50
        }}
        dataKey="value"
        isAnimationActive={false}
        data={Userdata}
        cx="50%"
        cy="50%"
        outerRadius={100}
        fill="#8884d8"
        label
      />
      <Tooltip />
      </PieChart>

      <LineChart
       width={500}
       height={300}
       data={Userdata}
       margin={{
         top: 5,
         right: 30,
         left: 50,
         bottom: 5,
       }}
     >
       <CartesianGrid strokeDasharray="3 3" />
       <XAxis dataKey="name" />
       <YAxis />
       <Tooltip />
       <Legend />
       <Line type="monotone" dataKey="value" stroke="#8884d8" activeDot={{ r: 8 }} />
       
     </LineChart>

    </div>
  );
}

export default Chart;