// let 변수명1 = 1;
// let 변수명2 = 2

// export { 변수명1, 변수명2 };

import { Alert } from 'bootstrap';
import { Navbar, Container, Nav } from 'react-bootstrap';
import { useEffect, useState } from 'react';
import { Routes, Route, Link, useNavigate, Outlet, useParams } from 'react-router-dom'
import styled from 'styled-components'
import { addItem } from './../store.js';
import { useDispatch } from 'react-redux';



let Btn =  styled.button`
  background : ${props => props.bg};
  color : black;
  padding : 10px
`
let Box =  styled.div`
background : grey;
padding : 20px
`

export const data = [
  {
    id: 0,
    title: "White and Black",
    content: "Born in France",
    price: 120000,
  },
  {
    id: 1,
    title: "Red Knit",
    content: "Born in Seoul",
    price: 110000,
  },
  {
    id: 2,
    title: "Grey Yordan",
    content: "Born in the States",
    price: 130000,
  },
];


function Main({shoes}){
  return(
    <>  
    <div className='main-bg'>
      {/* <Box>
        <Btn bg = 'red'>버튼</Btn>
      </Box> */}
    </div>
    <button onClick={()=>{}}>정렬하기</button>
    <div className="container">
      <div className="row">
        {shoes.map(function(a, i){
          return(
            <Card shoes = {shoes[i]} i={i+1} key={i}></Card>
          )})
        }
      </div>
    </div>
  </>
  )
}

function Card({shoes}) {
  let navigate = useNavigate();

  const handleClick = (id) => {
    // 로컬 스토리지에 저장하는 로직
    const watchedItems = JSON.parse(localStorage.getItem('watched')) || [];
    if (!watchedItems.includes(id)) {
      watchedItems.push(id);
      localStorage.setItem('watched', JSON.stringify(watchedItems));
    }

    // 상세 페이지로 이동
    navigate(`/detail/${id}`);
  };

  return (
    <div className="col-md-4" onClick={() => handleClick(shoes.id)}>
      <img src={`https://codingapple1.github.io/shop/shoes${shoes.id + 1}.jpg`} width="80%" alt={shoes.title} />
      <h4>{shoes.title}</h4>
      <p>{shoes.price}원</p>
    </div>
  );
}

function Detail(props){

  let { id } = useParams();
  let 찾은상품 = props.shoes.find(function(x){
    return x.id == id
  });
  let [salealert, setSaleAlert] = useState(true);
  let [count, setCount] = useState(0) 
  let [tap, setTap] = useState(0) 
  let [inputvalue, setInputvalue] = useState('')
  let [fade2, setFade2] = useState('')
  let dispatch = useDispatch()

  useEffect(()=>{
    console.log('hi')
  })

  useEffect(()=>{
    let timer =  setTimeout(()=>{setSaleAlert(false)},2000)
    console.log(2)
    return ()=>{//clean up function
      console.log(1)
      clearTimeout(timer)
    }
  }, [])

  useEffect(()=>{
    if (isNaN(inputvalue) == true){
      alert('그러지 마세요')
    }
  }, [inputvalue])

  useEffect(()=>{
    setTimeout(() => {setFade2('end')}, 100);

    return()=>{
      setFade2('')
    }
  }, [])

  return (
    <div className={`container start ${fade2}`}>
      {salealert == true  // sale 상태가 true일 때만 할인 메시지를 보여줍니다.
      ?
        <div className="alert alert-warning">
          2초 이내 구매시 할인
        </div>
        :null
      }
      {count}
      <button onClick={()=>{setCount(count+1)}}>+1</button>
      <div className="row">
        <div className="col-md-6">
          <img src={`https://codingapple1.github.io/shop/shoes1.jpg`} width="80%" alt='#' />
        </div>
        <div className="col-md-6 mt-4">
          <input onChange={(e)=>{setInputvalue(e.target.value)}} />
          <h4 className="pt-5">{찾은상품.title}</h4>
          <p>{찾은상품.content}</p>
          <p>{찾은상품.price}원</p>
          <button className="btn btn-danger" onClick={()=>{
            dispatch(addItem({ id: 찾은상품.id, name: 찾은상품.title, count: 0 }))
            console.log(1)
          }}>주문하기</button>
        </div>
      </div>
      
    <Nav variant="tabs"  defaultActiveKey="link0">
      <Nav.Item>
        <Nav.Link eventKey="link0" onClick={()=>{setTap(0)}}>버튼0</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="link1" onClick={()=>{setTap(1)}}>버튼1</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="link2" onClick={()=>{setTap(2)}}>버튼2</Nav.Link>
      </Nav.Item>
    </Nav>
    <TapContent tap = {tap} />
  </div>
  )
}
function TapContent({tap, shoes}){

  let [fade, setFade] = useState('') 

  useEffect(()=>{
    setTimeout(() => {setFade('end')}, 100);

    return()=>{
      setFade('')
    }
  }, [tap])

  return(
  <div className={`start ${fade}`}>
    {[<div>내용1</div>, <div>내용2</div>, <div>내용3</div>][tap]}
  </div>
  )
  }

function About(){
  return(
    <div>
      <h4>회사정보임</h4>
      <Outlet></Outlet>
    </div>
  )
}

export { Main, Card, Detail, About};