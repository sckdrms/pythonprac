import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import {Button, Navbar, Container, Nav} from 'react-bootstrap';

function App() {
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
      <Button variant="primary">Primary</Button>{' '}
      <Data></Data>
    </div>
  );
}

function Data() {
  let [menu, setMenu] = useState(['홈화면', '공지화면', '패치화면'])
  let [day, setDay] = useState(['2월 19일', '2월 20일', '2월 21일'])
  
  return (
    <div className='data'>
      {menu.map((menuItem, i) => (
        <div key={i}>
          <h4>{menuItem}</h4>
          <h4>{day[i]}</h4>
        </div>
      ))}
    </div>
  );
}


export default App;
