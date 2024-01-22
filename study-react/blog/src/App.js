import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {

  let post = '강남 우동 맛집';
  let [name, 상호명변경] = useState(['엽기떡볶이', '신전떡볶이', '킹콩떡볶이'])
  let [logo, setLogo] = useState(['ReactBlog'])
  let [좋아요, 좋아요변경] = useState(0); 

  function 좋아요함수(){     }
  
  return (
    <div className="App">
      <div className='black-nav'>
        <h4 style={{color : 'white', fontSize : '20px'}}>{logo}</h4>
      </div>

      <button onClick={()=>{ 
          let copy = [...name];
          copy[2] = '킹콩털볶이'
          상호명변경(copy) }}>이름변경</button>

      <button onClick={()=>{ 
          let copy = [...name];
          copy = copy.sort();
          상호명변경(copy) }}>이름 정렬</button>

      <div className='list'>

        <h4>{name[0]} <span onClick={()=>{좋아요변경(좋아요+1)}}>👍</span> {좋아요} </h4>
        <p>2월 17일 발행</p>
        <h4>{name[1]}</h4>
        <p>2월 17일 발행</p>
        <h4>{name[2]} <button onClick={()=>{ 
          let copy = [...name];
          copy[2] = '킹콩털볶이'
          상호명변경(copy) }}></button></h4>
        <p>2월 17일 발행</p>

      </div>
    </div>
  );
}

export default App;
