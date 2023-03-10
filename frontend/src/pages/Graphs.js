import react, { useState, useRef , PureComponent} from 'react';
import { PieChart , Pie, BarChart, Bar,  LineChart, Line, Tooltip,CartesianGrid,XAxis,YAxis,Legend} from 'recharts';

function Graph() {
  // sample data to show off the graphs
  const data = [ {name:"facebook", value: 20, peakUsage: 1.4},
                 {name: "instagram", value: 15, peakUsage: 1.1},
                 {name: "snapchat", value: 10, peakUsage: 0.8}
                ]
  

  return (
    <div style={{textAlign: "center"}} > 
      
    <div className="graph_orientation">
   
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
         width={400}
         height={300}
         data={data}
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
       </div>


       <div>
       <div className="graph_orientation">
       <LineChart
       width={500}
       height={300}
       data={data}
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

     <LineChart
     width={500}
     height={300}
     data={data}
     margin={{
       top: 5,
       right: 30,
       left: 20,
       bottom: 5,
     }}
   >
     <CartesianGrid strokeDasharray="3 3" />
     <XAxis dataKey="name" />
     <YAxis yAxisId="left" />
     <YAxis yAxisId="right" orientation="right" />
     <Tooltip />
     <Legend />
     <Line yAxisId="left" type="monotone" dataKey= "value" stroke="#8884d8" activeDot={{ r: 8 }} />
     <Line yAxisId="right" type="monotone" dataKey="peakUsage" stroke="#82ca9d" />
   </LineChart>
   </div>
       </div>
      
 </div>

  );
}

export default Graph;