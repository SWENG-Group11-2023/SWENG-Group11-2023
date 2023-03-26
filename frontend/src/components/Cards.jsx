import React from 'react'
import {Box, Card, CardContent, Typography, CardActions, Button, Stack} from '@mui/material';
import Graph from '../pages/Graphs';
import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import download from './Download';

const Cards = () => {
  const percentage = 66;

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
             <CircularProgressbar value={66} text={`${percentage}%`} />
            </div>  
          </Typography>
        </CardContent>
        <CardActions>
          <Button handleClick={download} size='small'>Download</Button>
          <Button size='small'>Learn more</Button>
        </CardActions>
      </Card>
    </Box>

    <Box width = '30%'>
            <Card>
        <CardContent>
          <Typography gutterBottom variant ='h5' component='div'>react
          </Typography>
          <Typography variant = 'body2' color='skyblue'>
          <div style={{ width: 100, height: 100 }}>
            <CircularProgressbar value={34} text={`34%`}/>
          </div>

          </Typography>
        </CardContent>
        <CardActions>
          <Button handleClick={download} size='small'>Download</Button>
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
            this is a better layout!
          </Typography>
        </CardContent>
        <CardActions>
          <Button handleClick={download} size='small'>Download</Button>
          <Button size='small'>Learn more</Button>
        </CardActions>
      </Card>
    </Box>
    
    </Stack>
    </div>
  )
}

export default Cards
