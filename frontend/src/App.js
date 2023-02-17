
import {useState} from 'react';
import useFetch from './useFetch'
import "./App.css";

const SearchBar = () => {
  const [message, setMessage] = useState('');


  const handleKeyDown = event => {
    console.log(event.key);

    if (event.key === 'Enter') {
      
      event.preventDefault();
      console.log(message);
      // console.log(event.target.value)

      console.log('User pressed Enter ✅');
      console.log("Typed Word :" + message);
    }
  }


  
  return (
    <div>
       <p >Search bar!</p>
       
      <input
        type="text"
        id="message"
        name="message"
        value={message}
        onChange={event => setMessage(event.target.value)}
        onKeyDown={handleKeyDown}
        message =""
      />
      <p>You typed: {message}</p>
    </div>
  );
};

function App(){
  const {data, loading, error} = useFetch("https://v2.jokeapi.dev/joke/Any%22");
  if(loading){
    return <h1>LOADING ...</h1>
  }
  if(error){
    return <h1>ERROR</h1>
  }

   if(data) {
    return (
     <div>
        <h1>{data.setup} : {data.delivery}</h1>
        </div>
      
    );
  }
}

const workingPage = {
  SearchBar,
  App
}
 export default workingPage;

