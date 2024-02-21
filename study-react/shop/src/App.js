import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import {Navbar, Container, Nav} from 'react-bootstrap';
// import bg from './img/bg.png';
import { data, Main, Card, Detail, About } from './components/data.js'
import {Routes, Route, Link, useNavigate, Outlet} from 'react-router-dom'



function App() {
  let [shoes] = useState(data)
  let navigate = useNavigate();

  return (
    <div className="App">
      <Navbar data-bs-theme="dark" className='nav-color'>
        <Container>
          <Navbar.Brand href="/">Changgeun Shop</Navbar.Brand>
          <Nav className="me-auto">
            {/* <Link to={'/'} className='Navlink'>Home</Link>
            <Link to={'/detail'} className='Navlink'>Detail</Link> */}
            <Nav.Link onClick={()=>{navigate('/')}}>home</Nav.Link>
            <Nav.Link onClick={()=>{navigate('/detail')}}>detail</Nav.Link>
            <Nav.Link onClick={()=>{navigate('/about')}}>about</Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      <Routes>
        <Route path='/' element={<Main shoes={shoes}></Main>} />
        <Route path='/detail/:id' element={ <Detail shoes={shoes}></Detail>} />
        <Route path='/about' element={ <About></About>}>
          <Route path='member' element={ <div>대표: 김창근</div>} />
          <Route path='skill' element={ <div>트월킹 고수</div>} />
        </Route>
        <Route path='*' element={ <div>없는 페이지랑께요</div>} />
      </Routes>


    </div>
  );

}



export default App;
