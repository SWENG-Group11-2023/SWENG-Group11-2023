import React from 'react'
import { Box, Card, CardContent, Typography, CardActions, Button, Stack } from '@mui/material';
import Graph from '../pages/Graphs';
import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import { DataFetching, updatedQuery, data } from "../pages/DataFetching";
import { useState } from 'react';


const Cards = () => {
    const [Userdata, setData] = useState([
        { mean: '79.678' },
        { median: '80.0' },
        { maximum: '100.0' },
        { minimum: '60.0' },
        { range: '40.0' },
        { stdev: '11.596' }
    ]);

    const [chartSummary, setSummary] = useState(['Default']);

    const updateData = () => {
        const newData = data.data.metrics;
        const summary = data.data.summary;
        console.log(data.data.metrics)
        setData(newData);
        setSummary(summary)
    };
    return (
        <div>
            <div>
                <Typography variant='h1' color={'skyblue'} borderBottom={true}>
                    <h2>
                        {chartSummary}
                    </h2>
                </Typography>
            </div>
            <Stack direction='row' spacing={16}>
                <Box width='13%'>
                    <Card>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                            </Typography>
                            <Typography variant='body2' color='skyblue'>
                                Average
                                <h1>
                                    {Userdata[0].mean}
                                </h1>
                            </Typography>
                        </CardContent>
                    </Card>
                </Box>

                <Box width='13%' >
                    <Card>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                            </Typography>
                            <Typography variant='body2' color='skyblue'>
                                Maximum
                                <h1>
                                    {Userdata[2].maximum}
                                </h1>
                            </Typography>
                        </CardContent>
                    </Card>
                </Box>

                <Box width='13%' >
                    <Card>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                            </Typography>
                            <Typography variant='body2' color='skyblue'>
                                Minimum
                                <h1>
                                    {Userdata[3].minimum}
                                </h1>
                            </Typography>
                        </CardContent>
                    </Card>
                </Box>

                <Box width='13%' >
                    <Card>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                            </Typography>
                            <Typography variant='body2' color='skyblue'>
                                Median
                                <h1>
                                    {Userdata[1].median}
                                </h1>
                            </Typography>
                        </CardContent>
                    </Card>
                </Box>

                <Box width='13%' >
                    <Card>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                            </Typography>
                            <Typography variant='body2' color='skyblue'>
                                StDev
                                <h1>
                                    {Userdata[5].stdev}
                                </h1>
                            </Typography>
                        </CardContent>
                    </Card>
                </Box>
            </Stack>
            <div>
                <Button size='large' onClick={updateData}>Update Cards</Button>
            </div>
        </div>
    )
}

export default Cards