import React, { useState } from 'react';
import { data } from './DataFetching';
import { BarChart, Bar, LineChart, Line, Tooltip, CartesianGrid, XAxis, YAxis, Legend } from 'recharts';
import { Button, Stack } from '@mui/material';

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
        <div>
            <div>
                <Button size='large' onClick={updateData}>Update Chart</Button>
            </div>
            <div className="graph_orientation">
                <Stack direction={'row'}>
                    <BarChart
                        width={600}
                        height={400}
                        data={Userdata}
                        margin={{
                            top: 5,
                            right: 30,
                            left: 70,
                            bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3" />
                        <Bar dataKey="value" fill="#8884d8" />
                        <XAxis dataKey="name" />
                        <YAxis dataKey="value" type="number" />
                        <Tooltip />

                    </BarChart>

                    <LineChart
                        width={600}
                        height={400}
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
                </Stack>

            </div>
        </div>
    );
}

export default Chart;