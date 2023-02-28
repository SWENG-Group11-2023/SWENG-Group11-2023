import react, { useState, useRef , PureComponent} from 'react';
import { PieChart , Pie, BarChart, Bar,  LineChart, Line,} from 'recharts';

function Graph() {
  const data = [ {name:"facebook", value: 20},
                 {name: "instagram", value: 15},
                 {name: "snapchat", value: 10}
                ]
  

  return (
    <>
        <BarChart width={150} height={40} data={data}>
          <Bar dataKey="value" fill="#8884d8" />
        </BarChart>
        <PieChart width={400} height={400}>
          <Pie
            dataKey="value"
            isAnimationActive={false}
            data={data}
            cx="30%"
            cy="40%"
            outerRadius={80}
            fill="#8884d8"
            label
          />
        </PieChart>
        <LineChart width={300} height={100} data={data}>
          <Line type="monotone" dataKey="pv" stroke="#8884d8" strokeWidth={2} />
        </LineChart>
    </>
  );
}

export default Graph;