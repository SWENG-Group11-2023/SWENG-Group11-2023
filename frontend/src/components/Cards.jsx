import React from 'react'
import { Box, Card, CardContent, Typography, CardActions, Button, Stack } from '@mui/material';
import Graph from '../pages/Graphs';
import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import { DataFetching, updatedQuery, data } from "../pages/DataFetching";
import { useState } from 'react';


const Cards = () => {
    const [Userdata, setData] = useState([
        { average: '79.678' },
        { median: '80.0' },
        { max: '100.0' },
        { min: '60.0' },
        { range: '40.0' },
        { standarddeviation: '11.596' }
    ]);

    const updateData = () => {
        const newData = data.data.metrics;
        console.log(data.data.metrics)
        setData(newData);
    };
    return (
        <div>
            <Stack direction='row' spacing={16}>
                <Box width='12%'>
                    <Card>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                            </Typography>
                            <Typography variant='body2' color='skyblue'>
                                Average
                                <h1>
                                    {Userdata[0].average}
                                </h1>
                            </Typography>
                        </CardContent>
                    </Card>
                </Box>

                <Box width='12%' >
                    <Card>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                            </Typography>
                            <Typography variant='body2' color='skyblue'>
                                Maximum
                                <h1>
                                    {Userdata[2].max}
                                </h1>
                            </Typography>
                        </CardContent>
                    </Card>
                </Box>

                <Box width='12%' >
                    <Card>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                            </Typography>
                            <Typography variant='body2' color='skyblue'>
                                Minimum
                                <h1>
                                    {Userdata[3].min}
                                </h1>
                            </Typography>
                        </CardContent>
                    </Card>
                </Box>

                <Box width='12%' >
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

                <Box width='12%' >
                    <Card>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                            </Typography>
                            <Typography variant='body2' color='skyblue'>
                                StDev
                                <h1>
                                    {Userdata[5].standarddeviation}
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
