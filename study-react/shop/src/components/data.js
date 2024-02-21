// let 변수명1 = 1;
// let 변수명2 = 2

// export { 변수명1, 변수명2 };

import { useState } from 'react';
import {Routes, Route, Link, useNavigate, Outlet, useParams} from 'react-router-dom'

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

function Card(props){
  return (
      <div className="col-md-4">
        <img src={`https://codingapple1.github.io/shop/shoes`+props.i+`.jpg`} width="80%" alt='#' />
        <h4>{props.shoes.title}</h4>
        <p>{props.shoes.price}</p>
      </div>
  );
}

function Detail(props){

  let {id} = useParams();

  return(
  <div className="container">
    <div className="row">
      <div className="col-md-6">
        <img src="https://codingapple1.github.io/shop/shoes1.jpg" width="100%" />
      </div>
      <div className="col-md-6">
        <h4 className="pt-5" key={id}>{props.shoes[id].title}</h4>
        <p>{props.shoes[id].content}</p>
        <p>{props.shoes[id].price}</p>
        <button className="btn btn-danger">주문하기</button> 
      </div>
    </div>
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