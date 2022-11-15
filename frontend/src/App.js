import './App.css';
import React, {useState} from 'react';
import axios from 'axios';
import ProgressBar from 'react-bootstrap/ProgressBar';

function App() {
  const [Status, setStatus] = useState({});

  function getData() {
    axios({
      method: 'GET',
      url: 'http://127.0.0.1:5000/',
    }).then((response) => {
      const res = response.data
      console.log(res.artist_name)
      setStatus(res)
    }).catch(error => {
        if(error.response) {
          console.log(error)
        }
      })
    };

  function BasicExample() {
    return <ProgressBar now={60} />;
  };

  return (
    <div className="App">
      <header className="App-header">
        {getData()}
        <p>Profile</p>
        {Status.is_playing && <div>
          <p>Artist Name: {Status.artist_name}</p>
          <p>Song Name: {Status.song_name}</p>
          <p>Image</p>
          <a href={Status.song_url}>
            <img src={Status.image_url} alt="Jacket" width="300"></img>
          </a>
          <p>Current Time: {Status.current_time_min}:{Status.current_time_sec<10 && <a>0</a>}{Status.current_time_sec}</p>
          <p>Whole Time: {Status.total_time_min}:{Status.total_time_sec<10 && <a>0</a>}{Status.total_time_sec}</p>
        </div>
        }
        {!Status.is_playing && <div>
          <p>USER is currently offline! Comeback later :)</p>
        </div>}
      </header>
    </div>
  );
}

export default App;