import { useState } from 'react';
import './App.css';
import data from './data'

function App() {

  let [shoes] = useState(data)

  return (
    <div className="App">
      <Shoes0 shoe = {shoes[0]}/>
    </div>
  );
}

function Shoes0(props) {
  return( <div>
    <p>{props.shoe.id}</p>
    <p>dd</p>
    <p></p>
  </div>
  )
}

export default App;
