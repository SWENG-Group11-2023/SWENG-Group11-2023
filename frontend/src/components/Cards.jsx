import React from 'react'
import {Box, Card, CardContent, Typography, CardActions, Button, Stack} from '@mui/material';
import Graph from '../pages/Graphs';
import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import DownloadButton from './DownloadCSV';
import { DataFetching, updatedQuery, data } from "../pages/DataFetching";
import  { useState } from 'react';


const Cards = () => {
  const [Userdata, setData] = useState([
        {average: '79.678'},
        {median: '80.0'},
        {max: '100.0'},
        {min: '60.0'},
        {range: '40.0'},
        {standarddeviation: '11.596'}
  ]);

  const updateData = () => {
    const newData = data.data.metrics;
      console.log(data.data.metrics)
    setData(newData);
  };
  return (
  <div>
    <Stack direction ='row' spacing={2}>
    <Box width = '30%' >
      <Card>
        <CardContent>
          <Typography gutterBottom variant ='h5' component='div'>react
          </Typography>
          <Typography variant = 'body2' color='skyblue'>
            <div style={{ width: 100, height: 100 }}>
             <CircularProgressbar value={66}/>
            </div>  
          </Typography>
        </CardContent>
        <CardActions>
          <DownloadButton/>
        </CardActions>
      </Card>
    </Box>

    <Box width = '30%'>
        <Card>
        <CardContent>
          <Typography gutterBottom variant ='h5' component='div'> {Userdata.summary}
          </Typography>
          <Typography variant = 'body2' color='skyblue'>
          <div style={{ width: 100, height: 100 }}>
            average
           <h1>{Userdata[0].average}</h1>
          </div>
          </Typography>
        </CardContent>
        <CardActions>
          <Button size='small' onClick={updateData}>update</Button>
          <Button size='small'>Learn more</Button>
        </CardActions>
      </Card>
    </Box>

    <Box width = '30%' >
      <Card>
        <CardContent>
          <Typography gutterBottom variant ='h5' component='div'>react
          </Typography>
          <Typography variant = 'body2' color='skyblue'>
          max
           <h1>{Userdata[2].max}</h1>
          </Typography>
        </CardContent>
        <CardActions>
          <Button size='small'>Learn more</Button>
        </CardActions>
      </Card>
    </Box>
    
    </Stack>
    </div>
  )
}

export default Cards
