
import {useState} from 'react';

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
  };

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


export default SearchBar;