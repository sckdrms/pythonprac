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
  return(
    <div>
      {props.shoe.map(function(shoe, index){
        return(
          <div key={index}>
            <p>{shoe.id}</p>
            <p>{shoe.title}</p>
            <p>{shoe.content}</p>
            <p>{shoe.price}</p>
          </div>
        );
      })}
    </div>
  );
}

export default App;
