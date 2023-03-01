import react, { useState, useRef , PureComponent} from 'react';
import { PieChart , Pie, BarChart, Bar,  LineChart, Line, Tooltip,CartesianGrid,XAxis,YAxis,Legend} from 'recharts';

function Graph() {
  const data = [ {name:"facebook", value: 20},
                 {name: "instagram", value: 15},
                 {name: "snapchat", value: 10}
                ]
  

  return (
    <div style={{textAlign: "center"}}  > 
  
    <div className="graph_orientation">

    
    <PieChart width={350} height={350}>
    
    <Pie
      
      margin ={{
        top: 20,
        right: 20,
        left: 20,
        bottom: 20
      }}
      dataKey="value"
      isAnimationActive={false}
      data={data}
      cx="50%"
      cy="50%"
      outerRadius={80}
      fill="#8884d8"
      label
    />
    <Tooltip />
  </PieChart>
  <BarChart
          width={350}
          height={350}
          data={data}
          margin={{
            top: 20,
            right: 20,
            left: 20,
            bottom: 20,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="value" fill="#8884d8" />
        
        </BarChart>
        </div>
        <div>
        <LineChart
        width={350}
        height={350}
        data={data}
        margin={{
          top: 20,
          right: 20,
          left: 10,
          bottom: 20,
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
        
  </div>

  );
}

export default Graph;