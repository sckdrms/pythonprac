import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {

  let post = '강남 우동 맛집';
  let [a, b] = useState(['엽기떡볶이', '신전떡볶이', '킹콩떡볶이'])
  let [logo, setLogo] = useState(['ReactBlog'])

  
  return (
    <div className="App">
      <div className='black-nav'>
        <h4 style={{color : 'white', fontSize : '20px'}}>{logo}</h4>
      </div>
      <div className='list'>
        <h4>{a[0]} </h4>
        <p>2월 17일 발행</p>
        <h4>{a[1]}</h4>
        <p>2월 17일 발행</p>
        <h4>{a[2]}</h4>
        <p>2월 17일 발행</p>
      </div>
    </div>
  );
}

export default App;
