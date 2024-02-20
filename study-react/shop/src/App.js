import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import {Button, Navbar, Container, Nav} from 'react-bootstrap';
// import bg from './img/bg.png';
import data from './data.js'



function App() {

  let [shoes] = useState(data)

  return (
    <div className="App">
      <Navbar data-bs-theme="dark" className='nav-color'>
        <Container>
          <Navbar.Brand href="#home">경운이들</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">홈</Nav.Link>
            <Nav.Link href="#features">공지사항</Nav.Link>
            <Nav.Link href="#pricing">패치노트</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      {/* <div className='main-bg' style={{backgroundImage : 'url('+ bg + ')'}}> */}
      <div className='main-bg'>
      </div>
      <div className="container">
          <div className="row">
            {/* <Shoe1></Shoe1>
            <Shoe2></Shoe2>
            <Shoe3></Shoe3> */}
            {/* <Shoe0 shoe={shoes[0]} />
            <Shoe1 shoe={shoes[1]} />
            <Shoe2 shoe={shoes[2]} /> */}
            {shoes.map((shoe, index) => (
            <ShoeComponent key={shoe.id} shoe={shoe} index={index} />
          ))}
          </div>
        </div> 
      {/* <Day1Data></Day1Data> */}
      {/* <img src={process.env.PUBLIC_URL + '/logo192.png'} />  */}
    </div>
  );

}

function Shoe0(props) {
  return (
    <div className="col-md-4">
      <img src="https://codingapple1.github.io/shop/shoes1.jpg" width="80%"/>
      <h4>{props.shoe.title}</h4>
      <p>{props.shoe.price}</p>
    </div>
  );
}

function ShoeComponent(props) {
  const { shoe, index } = props;
  return (
    <div className="col-md-4">
      <img src={`https://codingapple1.github.io/shop/shoes${index + 1}.jpg`} width="80%" alt={shoe.title}/>
      <h4>{shoe.title}</h4>
      <p>{shoe.price}원</p>
    </div>
  );
}

// function Shoe1(props) {
//   return (
//     <div className="col-md-4">
//       <img src="https://codingapple1.github.io/shop/shoes2.jpg" width="80%"/>
//       <h4>{props.shoe.title}</h4>
//       <p>{props.shoe.price}</p>
//     </div>
//   );
// }

// function Shoe2(props) {
//   return (
//     <div className="col-md-4">
//       <img src="https://codingapple1.github.io/shop/shoes3.jpg" width="80%"/>
//       <h4>{props.shoe.title}</h4>
//       <p>{props.shoe.price}</p>
//     </div>
//   );
// }

// function Day1Data() {
//   let [menu, setMenu] = useState(['홈화면', '공지화면', '패치화면'])
//   let [day, setDay] = useState(['2월 19일', '2월 20일', '2월 21일'])
  
//   return (
//     <div className='data'>
//       {menu.map((menuItem, i) => (
//         <div key={i}>
//           <h4>{menuItem}</h4>
//           <h4>{day[i]}</h4>
//         </div>
//       ))}
//     </div>
//   );
// }

// function Shoe1(props) {
//   return <div className="col-md-4">
//     <img src="https://codingapple1.github.io/shop/shoes1.jpg" width="80%" />
//     <h4>{props.shoes[0].title}</h4>
//     <p>{props.shoes[0].price}</p>
//   </div>;
// }

// function Shoe2(props) {
//   return <div className="col-md-4">
//     <img src="https://codingapple1.github.io/shop/shoes2.jpg" width="80%" />
//     <h4>{props.shoes[1].title}</h4>
//     <p>{props.shoes[1].price}</p>
//   </div>;
// }

// function Shoe3(props) {
//   return <div className="col-md-4">
//     <img src="https://codingapple1.github.io/shop/shoes3.jpg" width="80%" />
//     <h4>{props.shoes[2].title}</h4>
//     <p>{props.shoes[2].price}</p>
//   </div>;
// }


export default App;
